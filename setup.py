from setuptools import find_packages, setup

with open("VERSION") as f:
    version = f.read().strip()

with open("README.md") as fh:
    readme = fh.read()

setup(
    name='logger_lib',
    version=version,
    author='Saidur Rahman Sajol',
    description="Python library for custom logger",
    license='Proprietary',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/scorchSupernova/logger_lib",
    install_requires=[
        'Django'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
    ],

)