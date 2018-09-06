 #!/bin/bash 

python -m baselines.run \
--alg=ppo2 \
--num_timesteps=10000000 \
--network=mlp \
--env=Humanois-v2 \
--num_env=1 \
--save_folder=results/play \
--load_path=results/testfolder/final/ppo2 \
#--play \
#--load_path=results/testfolderTf/final/ppo2 \
 