from setuptools import setup

setup(
    name="compare_csv",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        compare_csv=hello:cli
    ''',
)