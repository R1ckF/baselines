 #!/bin/bash 

python -m baselines.run \
--alg=a2c \
--num_timesteps=0 \
--network=mlp \
--env=Humanoid-v2 \
--num_env=1 \
--save_folder=results/play \
--play \
--load_path=results/results_1/a2c_mlp_Humanoid-v2_4/final/a2c \
#--play \
#--load_path=results/testfolderTf/final/ppo2 \
 