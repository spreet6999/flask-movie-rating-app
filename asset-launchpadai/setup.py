import setuptools
from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

long_description = readme

setup(
    name="launch",
    version="0.0.1",
    author="Mark Huntington",
    author_email="Mark_Huntington@mckinsey.com",
    description="This is a tool to help build dash apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantumblack/asset-launchpadai",
    py_modules=['hello'],
    packages=find_packages(exclude=["docs*", "tests*", "tools*", "features*"]),
    # install_requires=requires,
    entry_points='''
        [console_scripts]
        launch=launch_cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
