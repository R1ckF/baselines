#!/usr/bin/env python3

import tensorflow as tf
from baselines import logger
from baselines.common.cmd_util import make_mujoco_env, common_arg_parser
from baselines.acktr.acktr_cont import learn
from baselines.acktr.policies import GaussianMlpPolicy
from baselines.acktr.value_functions import NeuralNetValueFunction

def train(env_id, num_timesteps, seed,args):
    env = make_mujoco_env(env_id, seed,0,monitor=args.record)

    with tf.Session(config=tf.ConfigProto()):
        ob_dim = env.observation_space.shape[0]
        ac_dim = env.action_space.shape[0]
        with tf.variable_scope("vf"):
            vf = NeuralNetValueFunction(ob_dim, ac_dim)
        with tf.variable_scope("pi"):
            policy = GaussianMlpPolicy(ob_dim, ac_dim)

        learn(env, policy=policy, vf=vf,
            gamma=0.99, lam=0.97, timesteps_per_batch=2500,
            desired_kl=0.002,
            num_timesteps=num_timesteps, animate=False)

        env.close()

def main():
    args = common_arg_parser().parse_args()

    if not args.save_folder:
        args.save_folder = 'results/acktr_'+str(args.network)+'_'+str(args.env)
    logger.configure(dir=args.save_folder)
    train(args.env, args.num_timesteps, args.seed, args)

if __name__ == "__main__":
    main()
