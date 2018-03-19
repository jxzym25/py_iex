from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = 'Python module to get stock data from IEX API'

setup(
    name='py_iex',
    version='0.0.3',
    author='Jerry Chou',
    author_email='jxzym25@gmail.com',
    license='MIT',
    description='Python module to get stock data from IEX API',
    long_description=long_description,
    url='https://github.com/jxzym25/py_iex',
    keywords=['iex', 'py_iex', 'stock', 'price', 'finance', 'quotes'],
    packages=find_packages(exclude=['test_py_iex']),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

