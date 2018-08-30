 #!/bin/bash 

python -m baselines.run \
--alg=ppo2 \
--num_timesteps=0 \
--network=mlp \
--env=Hopper-v2 \
--num_env=1 \
--load_path=results/ppo2_mlp_Hopper-v2/final/ppo2 \
--play


 
## Atari: ob: Box(84, 84, 4) ac: Discrete(6) Mujoco: ob: Box(11,) ac: Box(3,)



