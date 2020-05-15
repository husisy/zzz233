from setuptools import setup, find_packages

setup(
    name='zzz',
    version='0.0.1',
    packages=find_packages('python'),
    package_dir={'':'python'},
    description='personal frequently used scripts, NEVER should used in public code',
    install_requires=['numpy'], #cupy-cuda101
)
