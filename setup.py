from setuptools import setup, find_packages

setup(
    name="clin_data_tools",
    version="0.1.0",
    description="A toolkit for clinical data validation and manipulation",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0",
        "openpyxl>=3.0"
    ],
    entry_points={
        "console_scripts": [
            "check-col=clin_data_tools.check_col:check_col",
        ],
    },
)
