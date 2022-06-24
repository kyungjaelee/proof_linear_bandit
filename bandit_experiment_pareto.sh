for i in {1..5}
do
    python3 bandit_experiment.py --noise pareto  --optim_type proof --samples 10000 --actions 10 --moment 1.8 --dimension 20 --seed $i &
    python3 bandit_experiment.py --noise pareto  --optim_type supbtc --samples 10000 --actions 10 --moment 1.8 --dimension 20 --seed $i &
    python3 bandit_experiment.py --noise pareto  --optim_type supbmm --samples 10000 --actions 10 --moment 1.8 --dimension 20 --seed $i &
    python3 bandit_experiment.py --noise pareto  --optim_type menu --samples 10000 --actions 10 --moment 1.8 --dimension 20 --seed $i &
    python3 bandit_experiment.py --noise pareto  --optim_type tofu --samples 10000 --actions 10 --moment 1.8 --dimension 20 --seed $i
done