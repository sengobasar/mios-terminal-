from setuptools import setup, find_packages

setup(
    name="mios",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "psutil",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "mios = mios.cli.main:main"
        ]
    }
)
