import time
import numpy as np
import scipy.optimize

def reg_lin_reg(x_data, y_data, x_list, p, lam=1.):
    n, dim = x_data.shape
    X = x_data
    A = X.T.dot(X) + lam*np.eye(dim)
    
    weight_hat = np.linalg.inv(A).dot(X.T.dot(y_data))
    est_mean_list = x_list.dot(weight_hat)
    return est_mean_list, weight_hat

# Static helper functions for Catoni's estimator
def _cal_ap(p):
    if p == 2:
        return 1./2.
    else:
        ap = (2.*(((2.-p)/(p-1.)) ** (1.-(2./p))) + ((2.-p)/(p-1.))**(2.-(2./p))) **(-p/2.)
        return ap

def _cal_psi(x, p):
    ap = _cal_ap(p)
    b = np.abs(x)
    c = np.sign(x)
    psi = c*np.log(ap*b**p + b + 1.)
    return psi

def catoni_lin_reg(x_data, y_data, x_list, p, beta=1.):
    n, dim = x_data.shape
    remainder = lambda x: np.sum(_cal_psi(beta*np.abs([x.dot(z) - y for z, y in zip(x_data,y_data)]),p))
    sol = scipy.optimize.minimize(remainder,x0=np.zeros((dim,)))

    weight_hat = sol.x
    est_mean_list = x_list.dot(weight_hat)
    return est_mean_list, weight_hat

def trunc_lin_reg(x_data, y_data, x_list, p, lam=1., beta=1.):
    n, dim = x_data.shape
    X = np.array(x_data)
    A = X.T.dot(X) + lam*np.eye(dim)
    Y = np.array(y_data)
    U, s, VT = np.linalg.svd(X)
    B = VT.T.dot(np.diag(1/np.sqrt(s**2 + lam))).dot(VT)
    C = VT.T.dot(np.diag(s/np.sqrt(s**2 + lam))).dot(U[:,:dim].T)

    weight_hat = B.dot([np.sum(np.where(np.abs(c*Y) <= beta, c*Y, 0.)) for c in C])
    est_mean_list = x_list.dot(weight_hat)
    return est_mean_list, weight_hat

def trunc_reg(x_data, y_data, x_list, p, lam=1.):
    n, dim = x_data.shape
    X = np.array(x_data)
    A = X.T.dot(X) + lam*np.eye(dim)
    Y = np.array(y_data)

    h = x_list.dot(np.linalg.inv(A)).dot(X.T)
    thrs = np.sum(np.abs(h)**p,axis=1)**(1./p)

    Y_hat = np.asarray([np.where(np.abs(x_test.dot(np.linalg.inv(A)).dot(X.T)*Y) <= z, Y, 0.) for x_test, z in zip(x_list,thrs)])
    est_mean_list = np.sum(x_list.dot(np.linalg.inv(A)).dot(X.T)*Y_hat,axis=1)
    return est_mean_list, None

def mom_lin_reg(x_data, y_data, x_list, p, lam=1., k=10):
    n, dim = x_data.shape
    m = n//k
    As = []
    ws = []

    random_indices = np.random.permutation(n)
    for r in range(m):
        selected_indices = random_indices[r*k:(r+1)*k]
        x_sub = x_data[selected_indices,:]
        y_sub = np.array(y_data)[selected_indices]

        X = np.array(x_sub)
        A = X.T.dot(X) + lam*np.eye(dim)
        Y = np.array(y_sub)

        As.append(A)
        ws.append(np.linalg.inv(A).dot(X.T).dot(Y))

    ri = []
    for wi in ws:
        rj_list = []
        for wj, Aj in zip(ws,As):
            rj_list.append((wi-wj).dot(Aj).dot(wi-wj))
        ri.append(np.median(rj_list))

    weight_hat = ws[np.argmin(ri)]
    est_mean_list = x_list.dot(weight_hat)
    return est_mean_list, weight_hat

def pro(x_data, y_data, x_list, p, lam=1., beta=1.):
    n, dim = x_data.shape    
    
    X = np.array(x_data)
    A = X.T.dot(X) + lam*np.eye(dim)
    Y = np.array(y_data)
    h = x_list.dot(np.linalg.inv(A)).dot(X.T)
    
    thrs = beta*np.sum(np.abs(h)**p,axis=1,keepdims=True)**(1./p)
    c = h*Y / thrs    
    d = _cal_psi(c, p)    
    est_mean_list = np.sum(thrs*d,axis=1)
    return est_mean_list, None