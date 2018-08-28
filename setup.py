from setuptools import setup, find_packages
from .emailtoolspython import __version__

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='emailtoolspython',
    packages=find_packages(),
    version=__version__,
    author="Everton Tomalok",
    author_email="evertontomalok123@gmail.com",
    description="A serie of methods to help you work with validation and extraction of e-mails",
    long_description=long_description.replace('<br>', ' '),
    url="https://github.com/EvertonTomalok/emailtoolspython",
    download_url='https://github.com/EvertonTomalok/emailtoolspython/archive/master.zip',
    keywords=['email', 'emails', 'tool', 'tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests>=2.19.1', 'beautifulsoup4>=4.4.0', 'emailtoolspython', 'selenium'],
    license="MIT",
)
