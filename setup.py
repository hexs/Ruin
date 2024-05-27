from setuptools import setup, find_packages

setup(
    name='ruin',
    version='2024.0.1',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ruin-hello = runt_hello:hello"
        ],
    },
)
