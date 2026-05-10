from setuptools import find_packages, setup


setup(
    name="end_to_end_mlops",
    version="0.0.1",
    author="Tausif Islam",
    author_email="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

