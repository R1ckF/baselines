 
folder=results_1
 python extract_results.py \
--folders $folder/a2c_mlp_Humanoid-v2_4 $folder/acktr_mlp_Humanoid-v2 \
$folder/ddpg_mlp_Humanoid-v2 $folder/ppo2_mlp_Humanoid-v2_1 \
$folder/ppo2_mlp_Humanoid-v2_4 $folder/trpo_mpi_mlp_Humanoid-v2_1 \
--names a2c_4 acktr_1 ddpg_1 ppo2_1 ppo2_4 trpo_1 \
--live