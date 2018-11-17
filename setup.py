from setuptools import setup

setup(
    name='ask',
    version='0.1',
    py_modules=['scratch'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        ask=scratch:main
    ''',
)