 #!/bin/bash 

python -m baselines.run \
--alg=ppo2 \
--num_timesteps=100000 \
--network=mlp \
--env=Ant-v2 \
--num_env=4 \
--save_folder=testfolder 


 
## Atari: ob: Box(84, 84, 4) ac: Discrete(6) Mujoco: ob: Box(11,) ac: Box(3,)



