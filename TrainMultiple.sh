 #!/bin/bash

# python -m baselines.run \
# --alg=a2c \
# --save_interval=10000 \
# --num_env=4 \
# --num_timesteps=10000000 \
# --network=cnn \
# --log_interval=1000 \
# --env=PongNoFrameskip-v4

python -m baselines.run \
--alg=ppo2 \
--save_interval=1000 \
--num_env=1 \
--num_timesteps=20 \
--nsteps=10 \
--nminibatches=2 \
--network=mlp \
--log_interval=1 \
--env=CartPole-v0 \
--value_network=copy \
--gamma=0.99 \
--lr=0.0003 \
--seed=0 \
--noptepochs=1 \



# ---------------------------------------
# | approxkl           | 8.983622e-05   |
# | clipfrac           | 0.0            |
# | eplenmean          | 86.3           |
# | eprewmean          | 86.3           |
# | explained_variance | -0.592         |
# | fps                | 364            |
# | latest reward      | 75             |
# | nupdates           | 131            |
# | policy_entropy     | 0.18434809     |
# | policy_loss        | -0.00040670886 |
# | serial_timesteps   | 16768          |
# | total_timesteps    | 16768          |
# | value_loss         | 126.75198      |



# python -m baselines.run \
# --alg=ppo2 \
# --save_interval=1000 \
# --num_env=1 \
# --num_timesteps=100000 \
# --nsteps=128 \
# --nminibatches=4 \
# --network=mlp \
# --log_interval=1 \
# --env=CartPole-v0 \
# --value_network=copy \
# --gamma=0.99 \
# --lr=0.0003 \
# --seed=0 \
# --noptepochs=4 \

# python -m baselines.run \
# --alg=acktr \
# --save_interval=2500 \
# --num_env=4 \
# --num_timesteps=10000000 \
# --network=cnn \
# --log_interval=250 \
# --env=PongNoFrameskip-v4
