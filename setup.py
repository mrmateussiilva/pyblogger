from setuptools import setup, find_packages

setup(
    name="pyblogger",
    version="0.1",
    packages=find_packages(),
    install_requires=["markdown", "jinja2", "pyyaml"],
    entry_points={
        "console_scripts": [
            "pyblogger=pyblogger.cli:main"
        ]
    },
)
