 #!/bin/bash 

python -m baselines.run \
--alg=a2c \
--save_interval=10000 \
--num_env=4 \
--num_timesteps=10000000 \
--network=cnn \
--log_interval=1000 \
--env=PongNoFrameskip-v4

python -m baselines.run \
--alg=ppo2 \
--save_interval=1000 \
--num_env=4 \
--num_timesteps=10000000 \
--network=cnn \
--log_interval=50 \
--env=PongNoFrameskip-v4

python -m baselines.run \
--alg=acktr \
--save_interval=2500 \
--num_env=4 \
--num_timesteps=10000000 \
--network=cnn \
--log_interval=250 \
--env=PongNoFrameskip-v4
