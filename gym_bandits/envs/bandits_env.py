import numpy as np
import gym

class MultiarmedBanditsEnv(gym.Env):
    """Environment for multiarmed bandits"""
    metadata = {'render.modes': ['human']}

    def __init__(self, nr_arms=10):
        super(MultiarmedBanditsEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(nr_arms)
        self.observation_space = gym.spaces.Discrete(1)
        self.state = 0
        self.reset()


    def step(self, action):
        assert self.action_space.contains(action)
        reward = np.random.randn(1) + self.values[action]

        return self.state, reward, False, {self.optimal}

    def reset(self):
        self.values = np.random.randn(self.action_space.n)
        self.optimal = np.argmax(self.values)
        return self.state

    def render(self, mode='human', close=False):
        print("You are playing a %d-armed bandit" % self.action_space.n)
