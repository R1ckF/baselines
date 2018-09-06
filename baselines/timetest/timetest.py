from baselines.common.runners import AbstractEnvRunner
from baselines.common import set_global_seeds
import time
import numpy as np
from baselines import logger

class Runner(AbstractEnvRunner):

    def __init__(self, env, model, nsteps=5, gamma=0.99):
        super().__init__(env=env, model=model, nsteps=nsteps)


    def run(self):
        mb_obs, mb_rewards, mb_actions, mb_values, mb_dones = [],[],[],[],[]
        mb_states = self.states
        for n in range(self.nsteps):
            actions = self.env.action_space.sample()
            mb_obs.append(np.copy(self.obs))
            mb_actions.append(actions)
            mb_dones.append(self.dones)
            obs, rewards, dones, infos = self.env.step(actions)
            self.dones = dones
            for n, done in enumerate(dones):
                if done:
                    self.obs[n] = self.obs[n]*0
            self.obs = obs
            mb_rewards.append(rewards)
            latest_reward =  sum(info['latest'] for info in infos)/float(len(infos))
        mb_dones.append(self.dones)

        return latest_reward

def learn( env, seed, total_timesteps,nsteps=5, log_interval=500,**alg_kwargs):

        set_global_seeds(seed)
        nenvs = env.num_envs
        class Model:
            def __init__(self):
                self.initial_state = 3

        model = Model()
        runner = Runner(env,model=model, nsteps=nsteps)

        nbatch = nenvs*nsteps
        tstart = time.time()
        nupdates = total_timesteps//nbatch+1
        for update in range(1, nupdates):
            latest_reward = runner.run()
            nseconds = time.time()-tstart
            fps = int((update*nbatch)/nseconds)
            esttime = time.strftime("%H:%M:%S", time.gmtime(nseconds/update*(nupdates-update)))
            if update % log_interval == 0 or update == 1:
                logger.record_tabular("nupdates", update)
                logger.record_tabular("total_timesteps", update*nbatch)
                logger.record_tabular("Latest Reward", latest_reward)
                logger.record_tabular("estimated time left", esttime)
                logger.record_tabular("time elapsed", time.strftime("%H:%M:%S", time.gmtime(nseconds)))
                logger.dump_tabular()
        env.close()
        return model
