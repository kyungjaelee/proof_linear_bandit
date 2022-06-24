for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 1 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 10 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 20 --scale 1.0 --samples 10000 --seed 5


for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.2 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.5 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type catoni --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type mom --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type pro --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type reg --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc_lin --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5

for i in {1..4}
do
    python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed $i &
done
python3 regression_experiment.py --optim_type trunc --noise weibull --moment 1.8 --dimension 5 --scale 1.0 --samples 10000 --seed 5
