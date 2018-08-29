 #!/bin/bash 

#  python extract_results.py \
#  --alg a2c acktr ppo2 trpo_mpi \
# --network cnn cnn cnn cnn \
# --env pong pong pong pong \
# --folder results \
# --plots 1 2 3 4

 python extract_results.py \
 --alg ppo2 \
--network mlp \
--env Humanoid-v2 \
--folder results \
--plots 1 2 3 4