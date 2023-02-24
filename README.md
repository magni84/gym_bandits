# Gym Bandits

A multi-armed bandits environment for Gymnasium.

## Installation instructions

Requirements: gymnasium and numpy

```
git clone https://github.com/magni84/gym_bandits.git
cd gym-gridworld
pip install -e .
```

## Usage
```
import gymnasium as gym
import gym_bandits

env = gym.make('MultiArmedBandits-v0') # 10-armed bandit
env = gym.make('MultiArmedBandits-v0', nr_arms=15) # 15-armed bandit
```


