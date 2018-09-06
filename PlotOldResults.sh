 #!/bin/bash 

folder=results/results_1
 python extract_results.py \
--folders  \
$folder/a2c_lstm_Humanoid-v2_1 $folder/a2c_lstm_Humanoid-v2_4 \
$folder/a2c_mlp_Humanoid-v2_1 $folder/a2c_mlp_Humanoid-v2_4 \
$folder/acktr_mlp_Humanoid-v2 $folder/ddpg_mlp_Humanoid-v2 \
$folder/ppo2_mlp_Humanoid-v2_1 $folder/ppo2_mlp_Humanoid-v2_4 \
$folder/trpo_mpi_mlp_Humanoid-v2_1 \
--names a2c_1_lstm a2c_4_lstm a2c_1_mlp a2c_4_mlp acktr_1 ddpg_1 ppo2_1 ppo2_4 trpo_1 \
--window 100 \
--plots 1 2 3 4

# folder=results/results_1
#  python extract_results.py \
# --folders $folder/timetest_Humanoid-v2_1 $folder/timetest_Humanoid-v2_4 \
# $folder/a2c_lstm_Humanoid-v2_1 $folder/a2c_lstm_Humanoid-v2_4 \
# $folder/a2c_mlp_Humanoid-v2_1 $folder/a2c_mlp_Humanoid-v2_4 \
# $folder/acktr_mlp_Humanoid-v2 $folder/ddpg_mlp_Humanoid-v2 \
# $folder/ppo2_mlp_Humanoid-v2_1 $folder/ppo2_mlp_Humanoid-v2_4 \
# $folder/trpo_mpi_mlp_Humanoid-v2_1 \
# --names time_1 time_4 a2c_1_lstm a2c_4_lstm a2c_1_mlp a2c_4_mlp acktr_1 ddpg_1 ppo2_1 ppo2_4 trpo_1 \
# --window 100 \
# --plots 1 2 3 4