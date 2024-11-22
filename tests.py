#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: Lei Zhang 
@license: Apache Licence 
@file: tests.py 
@time: 2024/11/20
@contact: leizh5@cisco.com
@site:  
@software: PyCharm 
"""
import doctest
from super_dict import SuperDict

dictA = {
    'key1': 'value1',
    'key2': {
        'key2-1': 'value2-1'
    },
    'key3': {
        'key3-1': {
            'key3-1-1': [1, 2, 3, 4, 5],
            'key3-1-2': 3,
            'key3-1-3': None
        }
    }
}

dictB = {
    'key3': {
        'key3-1': {
            'key3-1-2': 4
        }
    }
}

dictC = {
    'key': {
        "dot.key": 2
    }
}

dictD = {
    'key': {
        'key-1': [
            {
                'key-1-list-1': 1
            },
            {
                'key-2-list-2': [1, 2, 3, 4]
            }
        ]
    }
}

if __name__ == "__main__":
    globs = {
        'SuperDict': SuperDict,
        'dictA': dictA,
        'dictB': dictB,
        'dictC': dictC,
        'dictD': dictD,
    }
    doctest.testfile("README.md", globs=globs, verbose=True)
