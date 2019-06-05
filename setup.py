from setuptools import setup, find_packages

setup(
    name='ensaio',
    version='0.0.1',
    install_requires=['click'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ensaio = app_rotinas.cli:cli'],
    }
)
