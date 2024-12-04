from setuptools import setup

setup(
    name="rl-tetris",
    version="1.0",
    description="Reinforcement Learning Tetris",
    author="Jeremy Ng",
    packages=["rl-tetris"],
    package_dir={"rl-tetris": "src"},
    install_requires=[
        "rl-tetris",
        "pygame",
    ]
)
