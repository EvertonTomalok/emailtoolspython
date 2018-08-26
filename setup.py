from setuptools import setup, find_packages

setup(
    name='emailtoolspython',
    packages=find_packages(),
    version='1.0.0',
    author="Everton Tomalok",
    author_email="evertontomalok123@gmail.com",
    description="A serie of methods to help you work with validation and extraction of e-mails",
    url="https://github.com/EvertonTomalok/emailtoolspython",
    download_url='https://github.com/EvertonTomalok/emailtoolspython/archive/master.zip',
    keywords=['email', 'emails', 'tool', 'tools'],
    classifiers=[],
    install_requires=['requests>=2.19.1', 'beautifulsoup4>=4.4.0'],
    license="MIT",
)
