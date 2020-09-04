import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitstats",  # Replace with your own username
    version=os.environ.get("GITHUB_REF", "alpha"),
    author="Brandon Graham-Knight",
    author_email="brandongk@alumni.ubc.ca",
    description=
    "A package for calculating contributions and progress on GitHub projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandongk-ubco/gitstats",
    packages=setuptools.find_packages(),
    install_requires=['seaborn', 'PyGithub'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 (AGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
