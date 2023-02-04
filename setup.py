from setuptools import setup
setup(
    name = 'RevPicli',
    version = '0.1.0',
    packages = ['RevolutionPi'],
    entry_points = {
        'console_scripts': [
            'RevolutionPi = RevolutionPi.__main__:main'
        ]
    })