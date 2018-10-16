 #!/bin/bash 



## redo ppo2 mlp with copy value network
## try roboschool?
timesteps=1000000
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
# --value_network=copy \
# --record

# python -m baselines.run \
# --alg=a2c \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --value_network=copy \
# --record

# python -m baselines.run \
# --alg=trpo_mpi \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --record

python -m baselines.run \
--alg=ppo2 \
--num_timesteps=$timesteps \
--network=$net \
--env=$environment \
--num_env=4 \
--nsteps=1024 \
--value_network=None \
--record

# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=4 \
# --save_folder=results/ppo2_$environment_$net_4_2048steps_large_minibatch \
# --value_network=copy \
# --record

# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --nsteps=1024 \
# --value_network=copy \
# --record

python -m baselines.run \
--alg=acktr \
--num_timesteps=$timesteps \
--network=$net \
--env=$environment \
--num_env=4 \
--nsteps=1024 \
--value_network=copy \
--record

# python -m baselines.run \
# --alg=acktr \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --nsteps=1024 \
# --value_network=copy \
# --record

# net=lstm

# python -m baselines.run \
# --alg=a2c \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=4 \
# --nsteps=20 \
# --record

# python -m baselines.run \
# --alg=a2c \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --nsteps=20 \
# --record

# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=4 \
# --nsteps=20 \
# --record

# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --nsteps=20 \
# --record

# python -m baselines.run \
# --alg=acktr \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=4 \
# --nsteps=20 \
# --record

# python -m baselines.run \
# --alg=acktr \
# --num_timesteps=$timesteps \
# --network=$net \
# --env=$environment \
# --num_env=1 \
# --nsteps=20 \
# --record

python -m baselines.ddpg.main \
--env_id=$environment \




## Atari: ob: Box(84, 84, 4) ac: Discrete(6) Mujoco: ob: Box(11,) ac: Box(3,)

## tf takes 36:41 min on hopper 1000000 timesteps
## nontf takes 27 min on hopper 1000000 timesteps
