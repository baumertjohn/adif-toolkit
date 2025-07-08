from setuptools import setup, find_packages

setup(
    name="adiflib",
    version="0.1.0",
    packages=find_packages(),
    description="A Python library for processing ADIF files",
    author="John Baumert",
    author_email="baumert.john@gmail.com",
    url="https://github.com/baumertjohn/adif-toolkit",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
