from setuptools import setup, find_packages

setup(
    name="mutual_fund_tracker",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "boto3"
    ],
    entry_points={
        "console_scripts": [
            "mutual_fund_tracker=src.main:main"
        ]
    }
)