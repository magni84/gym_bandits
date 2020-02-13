from gym.envs.registration import register

register(
    id='MultiarmedBandits-v0',
    entry_point='gym_bandits.envs:MultiarmedBanditsEnv',
)
