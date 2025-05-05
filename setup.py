from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="archivertools",
    version="1.0.0",
    author="Andrea Pollastro",
    author_email="apollastro@lbl.gov",
    description="archivertools is a module to interact with the ALS archiver server through Python.",
    url="https://github.com/andrea-pollastro/als-archiver-client",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)