for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type catoni --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type catoni --samples 10000 --seed 5

for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type mom --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type mom --samples 10000 --seed 5

for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type pro --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type pro --samples 10000 --seed 5

for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type reg --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type reg --samples 10000 --seed 5

for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type trunc_lin --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type trunc_lin --samples 10000 --seed 5

for i in {1..4}
do
    python regression_experiment_movielens.py --optim_type trunc --samples 10000 --seed $i &
done
python regression_experiment_movielens.py --optim_type trunc --samples 10000 --seed 5

