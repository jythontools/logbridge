import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "logbridge",
    version = "0.1",
    packages = find_packages()
)
