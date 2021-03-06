import argparse
import os
import yaml
import gym
from gym import wrappers
from agents.a3c import A3CAgent
import dill as pickle
import torch.multiprocessing as mp
from envs.pong_env import PongSinglePlayerEnv
from wrappers.process_frame import AtariRescale42x42Wrapper
from wrappers.process_frame import NormalizeWrapper
from yaml import CLoader as Loader


def create_async_agent(conf, action_space, observation_space):
    if conf['agent'] == "a3c":
        return A3CAgent(
            action_space,
            observation_space,
            learning_rate=conf['learning_rate'],
            discount=conf['discount'],
            t_max=conf['t_max'])
    else:
        raise ArgumentError("AsyncAgent type [%s] is not supported." %
                            conf['agent'])
def create_env(conf, monitor_on=False):
    env = gym.make(conf['env'])
    if conf['monitor_dir'] != '' and monitor_on:
        env = wrappers.Monitor(env, conf['monitor_dir'], force=True)
    if conf['use_atari_wrapper']:
        env = AtariRescale42x42Wrapper(env)
        env = NormalizeWrapper(env)
    return env

def learn_thread(conf, master_agent, process_id):
    env = create_env(conf, monitor_on=process_id == 0)
    env.seed(process_id)
    slave_agent = master_agent.create_async_learner()
    slave_agent.reset()
    return_list = []
    for episode in range(conf['num_episodes_per_process']):
        cum_return = 0.0
        observation = env.reset()
        done = False
        while not done:
            action = slave_agent.act(observation)
            #action = action.to("cpu").numpy()
            next_observation, reward, done, _ = env.step(action)
            slave_agent.learn(reward, next_observation, done)
            observation = next_observation
            cum_return += reward
        return_list.append(cum_return)
        print("Episode %d/%d Return: %f." %
                (episode + 1, conf['num_episodes_per_process'], cum_return))
        # save checkpoints
        if process_id == 0 and episode % conf['checkpoint_freq'] == 0:
            model_filename = os.path.join(conf['checkpoint_dir'],
                                            'agent.model-%d' % episode)
            master_agent.save_model(model_filename)
    env.close()

def run_async(conf):
    print("----- Running job [%s] ----- " % conf['job_name'])

    env = create_env(conf)
    master_agent = create_async_agent(conf, env.action_space,
                                      env.observation_space)
    if conf['init_model_path'] != '':
        master_agent.load_model(conf['init_model_path'])
    env.close()

    processes = []
    #lock = mp.Lock()
    mp.set_start_method('spawn')
    master_agent._shared_model.share_memory()
    for process_id in range(0, conf['num_processes']):
        p = mp.Process(target=learn_thread, args=(conf, master_agent, process_id, ))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    
   # learn_thread(1)

if __name__ == '__main__':    
    os.environ['OMP_NUM_THREADS'] = '1'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Configuration file in ymal format.")
    args = parser.parse_args()

    conf = yaml.load(open(args.config, 'r'), Loader=Loader)

    if not os.path.exists(conf['checkpoint_dir']):
        os.mkdir(conf['checkpoint_dir'])

    run_async(conf)
