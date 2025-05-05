from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="als-archiver-client",
    version="1.0.0",
    author="Andrea Pollastro",
    author_email="apollastro@lbl.gov",
    description="A Python package for interacting with the ALS archiver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrea-pollastro/als-archiver-client",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.10',
    keywords="epics, archiver, data-mining, engineering, research, particle-accelerator",
)
