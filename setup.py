#!/usr/bin/env python3

import setuptools

def read(fname):
    with open(fname, 'r') as f:
        return f.read()

setuptools.setup(
    name="smartgadget",
    version="0.1",
    author="Alberto Sottile",
    author_email="alby128@gmail.com",
    description=' '.join([
        'Interact with a Sensirion SHT31 Smart Gadget',
        'Development Kit using the Bluetooth GATT SDK for Python'
    ]),
    url="https://github.com/albertosottile/SmartGadget-gatt",
    packages=['smartgadget'],
    install_requires=read('requirements.txt').splitlines(),
    python_requires=">=3.5",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering"
    ],
)
