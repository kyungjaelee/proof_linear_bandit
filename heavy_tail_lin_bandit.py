import numpy as np
from heavy_tail_regressions import _cal_psi, _cal_ap

def MENU(D, get_mean, get_observation, S=1., lamb=1., delta=0.01, p=1.5, c=1.):
    T, K, d=D.shape
    
    error_list = np.zeros((T,))
    
    # initialization
    epsilon = p - 1.
    k = int(np.ceil(24 * np.log(epsilon * T / delta)))
    N = np.maximum(int(T // k),1)
    V = lamb * np.eye(d)
    Vinv = np.linalg.inv(V)
    theta_star = np.zeros(d)
    x = np.zeros((N, d))
    y = np.zeros((N, k))
    beta = S
    cum_regret = 0

    # algorithm
    for n in range(N):
        # pick D_n
        Dt = D[n]
        Rt = get_mean(Dt, n)

        # line 4 : select an arm
        scores = Dt.dot(theta_star) + beta*np.sqrt(np.diag(Dt.dot(Vinv.dot(Dt.T))))
        at = np.argmax(scores)
        x[n] = Dt[at]

        # line 5 : observe payoffs
        y[n] = [get_observation(x[n], n, at) for _ in range(k)]

        # line 6 : update V
        V = V + x[n][:,np.newaxis]*x[n][np.newaxis,:]
        Vinv = np.linalg.inv(V)

        # line 7 : calculate LSE for the j-th group
        thetas = Vinv.dot(x[:(n+1),:].T.dot(y[:(n+1),:])).T

        # line 8 : find median
        r = []
        for j in range(k):
            r_med = []
            for s in range(k):
                delta_theta = thetas[j] - thetas[s]
                r_med.append(np.dot(np.dot(delta_theta.T, V), delta_theta))
            r.append(np.median(r_med))

        # line 9 : take median of means of estimates
        k_star = np.argmin(r)

        # line 10 : compute beta
        beta = 3 * (((9 * d * c) ** (1 / (1 + epsilon))) * ((n + 1) ** ((1 - epsilon) / (2 * (1 + epsilon)))) + (lamb ** (1 / 2)) * S)

        # line 11 : update the confidence region
        theta_star = thetas[k_star]

        # line 12 : Regret
        cum_regret += np.max(Rt) - Rt[at]
        
        # line 13 : Store errors
        if n==N-1:
            error_list[n*k:] = cum_regret/(n+1)
        else:
            error_list[n*k:np.minimum((n+1)*k,T)] = cum_regret/(n+1)
        
    return error_list, theta_star

def TOFU(D, get_mean, get_observation, S=1., lamb=1., delta=0.01, p=1.5, b=1.):
    T, K, d=D.shape
    
    epsilon=p-1.
    error_list = np.zeros((T,))
    
    # initialization
    V = lamb * np.eye(d)
    Vinv = np.linalg.inv(V)
    theta_star = np.zeros(d)
    x = np.zeros((T, d))
    y = np.zeros(T)
    beta = S
    cum_regret = 0

    # algorithm
    for t in range(T):
        # pick D_t
        Dt = D[t]
        Rt = get_mean(Dt, t)

        # line 4 : compute b_t
        b_t = ((b / (np.log(2 * T / delta))) ** (1 / epsilon)) * (t ** ((1 - epsilon) / (2 * (1 + epsilon))))

        # line 5 : select an arm
        scores = Dt.dot(theta_star) + beta*np.sqrt(np.diag(Dt.dot(Vinv.dot(Dt.T))))
        at = np.argmax(scores)
        x[t] = Dt[at]
        
        # line 6 : observe a payoff
        y[t] = get_observation(x[t], t, at)

        # line 7 : update V & define X
        V = V + x[t][:,np.newaxis]*x[t][np.newaxis,:]
        Vinv = np.linalg.inv(V)
        X_t = x[:t + 1, :]

        # line 8 : compute u
#         U_svd, sgv, VT_svd = np.linalg.svd(X_t)
#         Vinvsqrt = VT_svd[:t+1,:].T.dot(np.diag(1/np.sqrt(sgv**2 + lamb))).dot(VT_svd[:t+1,:])
#         u = VT_svd[:t+1,:].T.dot(np.diag(sgv/np.sqrt(sgv**2 + lamb))).dot(U_svd[:,:d].T)
        
        A, Q = np.linalg.eig(Vinv)
        Vinvsqrt = np.dot(np.dot(Q, np.diag(np.sqrt(A))), Q.T)
        u = np.dot(Vinvsqrt, X_t.T)

        # line 9-12 : truncate the payoffs
#         print(b_t)
#         print([np.abs(u_d * y[:t + 1]) <= b_t for u_d in u])
        theta_dag = Vinvsqrt.dot([np.sum(np.where(np.abs(u_d * y[:t + 1]) <= b_t, u_d * y[:t + 1], 0.)) for u_d in u])

        # line 13 : compute beta
        beta = 4 * np.sqrt(d) * (b ** (1 / (1 + epsilon))) * (np.log(2 * d * T /  delta) ** (epsilon / (1 + epsilon))) * (t ** ((1 - epsilon) / (2 * (1 + epsilon)))) + (np.sqrt(lamb) * S)

        # line 14 : update the confidence region
        theta_star = theta_dag

        # line 12 : Regret
        cum_regret += np.max(Rt) - Rt[at]
        
        # line 13 : Store errors
        error_list[t] = cum_regret/(t+1)
        
    return error_list, theta_star

def pro(D, X, Y, p, beta=1., S=1., lamb=1., nu=1.):
    n, d = X.shape
    if n==0:
        X = np.zeros((1,d))
    
    ap = _cal_ap(p)
    
    A = X.T.dot(X) + lamb*np.eye(d)
    Ainv = np.linalg.inv(A)
    h = D.dot(Ainv.dot(X.T))
    thrs = beta*np.sum(np.abs(h)**p,axis=1,keepdims=True)**(1./p)
    
    c = h*Y / thrs    
    d = _cal_psi(c, p)    
    rhat = np.sum(thrs*d,axis=1)
    
    w = ((ap*nu+1)*beta+np.sqrt(lamb)*S)*np.sqrt(np.diag(D.dot(Ainv.dot(D.T))))
    return rhat, w
    

def btc(D, X, Y, p, alpha=1., lamb=1.):
    n, d = X.shape
    if n==0:
        X = np.zeros((1,d))
    
    A = X.T.dot(X) + lamb*np.eye(d)
    Ainv = np.linalg.inv(A)
    h = D.dot(Ainv.dot(X.T))
    thrs = np.sum(np.abs(h)**p,axis=1)**(1./p)
    Y_hat = np.asarray([np.where(np.abs(xt.dot(Ainv.dot(X.T))*Y) <= z, Y, 0.) for xt, z in zip(D,thrs)])
    rhat = np.sum(D.dot(Ainv.dot(X.T))*Y_hat,axis=1)
    w = (alpha+1)*np.sqrt(np.diag(D.dot(Ainv.dot(D.T))))
    
    return rhat, w    

def bmm(D, X, Y, alpha=1., lamb=1.):
    n, d = X.shape
    _, k = Y.shape
    if n==0:
        X = np.zeros((1,d))
        Y = np.zeros((1,k))
    
    A = X.T.dot(X) + lamb*np.eye(d)
    Ainv = np.linalg.inv(A)
    rhat = np.median(D.dot(Ainv.dot(X.T)).dot(Y),axis=1)
    w = (alpha+1)*np.sqrt(np.diag(D.dot(Ainv.dot(D.T))))
    
    return rhat, w    

def SupHvyLinBandit(D, get_mean, get_observation, method="proof", S=1., lamb=1., delta=0.01, nu = 1., p=1.5 ):
    T, K, d=D.shape
    if method in "proof":
        k = 1
        N = T
        x = np.zeros((N, d))
        y = np.zeros((N,))
        N_stage = np.maximum(int(np.log(T)*d**(1./2.-1./p)),1)
    elif method in "btc":
        k = 1
        N = T
        x = np.zeros((N, d))
        y = np.zeros((N,))
        N_stage = np.maximum(int(np.log(T)),1)
    elif method in "bmm":
        k = int(np.ceil(8 * np.log(2 * K * T / delta)))
        N = np.maximum(int(T // k),1)
        x = np.zeros((N, d))
        y = np.zeros((N, k))
        N_stage = np.maximum(int(np.log(T)),1)

    error_list = np.zeros((T,))
    Psi_t_s = [[] for _ in range(N_stage)]
    cum_regret = 0

    # algorithm
    for t in range(N):
        Dt = D[t]
        Rt = get_mean(Dt, t)

        if method in "btc":
            alpha_t = (2./3.*np.log(2*T*K*np.log(T)/delta)+np.sqrt(2*np.log(2*T*K*np.log(T)/delta)*nu) + nu)*t**((2.-p)/(2.*p))
        elif method in "proof":
            alpha_t = T**((2.-p)/(2.*p))*np.log(2*T*K/delta)**(-1./p)
        elif method in "bmm":
            alpha_t = (12.*nu)**(1/p)*t**((2.-p)/(2.*p))

        s=0
        action_set=list(range(K))
        a=-1
        while a < 0:
            if method in "btc":
                rhat, w = btc(Dt, x[Psi_t_s[s]], y[Psi_t_s[s]], p, alpha=alpha_t, lamb=lamb)
            elif method in "proof":
                rhat, w = pro(Dt, x[Psi_t_s[s]], y[Psi_t_s[s]], p, beta=alpha_t, S=S, lamb=lamb, nu=nu)
            elif method in "bmm":
                rhat, w = bmm(Dt, x[Psi_t_s[s]], y[Psi_t_s[s]], alpha=alpha_t, lamb=lamb)
                
            if np.all(w[action_set] <= 1/np.sqrt(T)):
                a = np.argmax(rhat[action_set]+w[action_set])
            elif np.any(w[action_set] > 2**(-(s+1))):
                candidates, = np.where(w[action_set] > 2**(-(s+1)))
                a = action_set[candidates[0]]
                Psi_t_s[s].append(t)
            else:
                Bmax = np.max(rhat[action_set]+w[action_set])
                action_set = [a for a in action_set if rhat[a]+w[a] > Bmax - 2**(-s)]
                s += 1
                
                if s >= N_stage:
                    a = np.random.choice(K,1)[0]
                    Psi_t_s[0].append(t)

        x[t] = Dt[a]
        if method in ["btc", "proof"]:
            y[t] = get_observation(x[t], t, a)
        elif method in "bmm":
            y[t] = [get_observation(x[t], t, a) for _ in range(k)]

        # line 12 : Regret
        cum_regret += np.max(Rt) - Rt[a]
        
        # line 13 : Store errors
        if method in ["btc", "proof"]:
            error_list[t] = cum_regret/(t+1)
        elif method in "bmm":
            if t==N-1:
                error_list[t*k:] = cum_regret/(t+1)
            else:
                error_list[t*k:np.minimum((t+1)*k,T)] = cum_regret/(t+1)
        
        
    return error_list, (Psi_t_s, x, y)