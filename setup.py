
from setuptools import setup

setup(name='expressiontree',
    version='0.01',
    description='A tool to study expressions from the CLI',
    url='https://github.com/Dual-Exhaust/ExpressionTree',
    author='Dual-Exhaust',
    author_email='kylecsacco@gmail.com',
    license='MIT',
    packages=['expressiontree'],
    scripts=['bin/buildtree'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False)
