from setuptools import setup, find_packages
setup(
    name="emailtoolspython",
    version="1.0.0",
    packages=find_packages(),

    install_requires=['requests>=2.19.1', 'bs4>=4.4.0'],

    # metadata to display on PyPI
    author="Everton Tomalok",
    author_email="evertontomalok123@gmail.com",
    description="A serie of methods to help you work with validation and extraction of e-mails",
    license="MIT",
    keywords="email emails tool tools python python3",
    url="https://github.com/EvertonTomalok/emailtoolspython"
)
