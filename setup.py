import setuptools
from setuptools import setup

setup(name='gym_bandits',
      version='0.0.1',
      author='Per Mattsson',
      author_email='magni84@gmail.com',
      description='Implements multi-armed bandits',
      url='https://github.com/magni84/gym_bandits',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
      install_requires=['gym', 'numpy']
)
