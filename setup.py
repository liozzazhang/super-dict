#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: Lei Zhang 
@license: Apache Licence 
@file: setup.py 
@time: 2024/11/18
@contact: liozza@163.com
@site:  
@software: PyCharm 
"""
import os
import sys

from setuptools import setup, find_packages
sys.path.insert(0, os.path.abspath('pkg'))
from super_dict import __program__, __desc__, __author__, __version__, __classifiers_deployment_status__, __email__


lib_folder = os.path.dirname(os.path.realpath(__file__))
requirementPath = lib_folder + '/requirements.txt'
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(
    name=__program__,
    version=__version__,
    description=__desc__,
    author=__author__,
    author_email=__email__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
    package_dir={'': 'pkg'},
    packages=find_packages('pkg'),
    install_requires=install_requires,
    data_files=[('', ['requirements.txt'])],
    classifiers=[
            __classifiers_deployment_status__,
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries',
            'Intended Audience :: Developers'
            ],
    # Installing as zip files would break due to references to __file__
    zip_safe=False
)
