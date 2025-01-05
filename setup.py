from setuptools import setup, find_packages

setup(
    name="clin_data_tools",
    version="0.1.0",
    description="A toolkit for clinical data validation and manipulation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
