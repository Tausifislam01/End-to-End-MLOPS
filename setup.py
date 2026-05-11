from setuptools import find_packages, setup


setup(
    name="mlProject",
    version="0.0.1",
    author="Tausif Islam",
    author_email="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

