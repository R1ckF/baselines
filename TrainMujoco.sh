 #!/bin/bash 

timesteps=10000
environment=Hopper-v2
net=mlp

# python -m baselines.run \
# --alg=timetest \
# --num_timesteps=$timesteps \
# --env=$environment \
# --num_env=4 \
# --record

# python -m baselines.run \
# --alg=timetest \
# --num_timesteps=$timesteps \
# --env=$environment \
# --num_env=1 \
# --record


# python -m baselines.run \
# --alg=a2c \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=4 \
# --record

python -m baselines.run \
--alg=ppo2 \
--num_timesteps=$timesteps \
--network=$net \
--env=$environment \
--num_env=4 \
--nsteps=1024 \
--record

# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --record

# python -m baselines.acktr.run_mujoco \
# --num_timesteps=$timesteps \
# --network= \
# --env=$environment \
# --num_env=1 \
# --record



# python -m baselines.run \
# --alg=trpo_mpi \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --record

# python -m baselines.run \
# --alg=a2c \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --record

# python -m baselines.ddpg.main \
# --env_id=$environment \



## Atari: ob: Box(84, 84, 4) ac: Discrete(6) Mujoco: ob: Box(11,) ac: Box(3,)

## tf takes 36:41 min on hopper 1000000 timesteps
## nontf takes 27 min on hopper 1000000 timesteps
