#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kinesthesis-2.0",
    version="1.0.0",
    author="Telemachus Moussas",
    author_email="your.email@example.com",
    description="Gesture-controlled interactive vocal augmentation system using MediaPipe and Max/MSP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Kinesthesis-2.0",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "mediapipe>=0.10.0",
        "opencv-python>=4.8.0",
        "python-osc>=1.8.0",
        "numpy>=1.24.0",
        "scipy>=1.11.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
        "visualization": [
            "matplotlib>=3.8.0",
            "pandas>=2.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "kinesthesis-2.0=Kinesthesis_2_0:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/Kinesthesis-2.0/issues",
        "Source": "https://github.com/yourusername/Kinesthesis-2.0",
        "Documentation": "https://github.com/yourusername/Kinesthesis-2.0#readme",
    },
    keywords="gesture recognition hand tracking facial landmarks OSC Max/MSP vocal augmentation",
    zip_safe=False,
)
