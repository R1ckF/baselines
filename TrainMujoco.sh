 #!/bin/bash 


python -m baselines.run \
--alg=ppo2 \
--num_timesteps=10000 \
--network=mlp \
--env=Hopper-v2 \
--num_env=1 
#--env=Hopper-v2 
# python -m baselines.run \
# --alg=ppo2 \
# --num_timesteps=10000 \
# --network=mlp \
# --env=Hopper-v2 

# python -m baselines.run \
# --alg=trpo_mpi \
# --num_timesteps=10000 \
# --network=mlp \
# --env=Hopper-v2 

 
## Atari: ob: Box(84, 84, 4) ac: Discrete(6) Mujoco: ob: Box(11,) ac: Box(3,)



