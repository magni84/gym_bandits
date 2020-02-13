# Gym Bandits

A multi-armed bandits environment for OpenAI gym.

## Installation instructions

Requirements: gym and numpy

```
pip install gym-bandits
```

## Usage
```
import gym
import gym_bandits

env = gym.make('MultiArmedBandits-v0') # 10-armed bandit
env = gym.make('MultiArmedBandits-v0', nr_arms=15) # 15-armed bandit
```


