 #!/bin/bash 

python -m baselines.run \
--alg=ppo2 \
--num_env=4 \
--num_timesteps=200000 \
--network=mlp \
--env=InvertedPendulum-v2


