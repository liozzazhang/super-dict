#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: Lei Zhang 
@license: Apache Licence 
@file: structure_data.py 
@time: 2024/11/20
@contact: liozza@163.com
@site:  
@software: PyCharm 
"""
from typing import MutableMapping


def flatten_dict(d, parent_key='', sep='.', quiet=False):
    """
    Flat dict to one level dict.
    Use dot(.) in key to present level.

    :param d: dict
    :param parent_key: parent key
    :param sep: separator string
    :param quiet: do not raise error
    :return: flatten dict
    :rtype: dict
    """
    items = []
    for k, v in d.items():

        if not quiet and sep in k:
            raise ValueError('Separator "%(sep)s" already in key, '
                             'this may lead unexpected behaviour, '
                             'choose another.' % dict(sep=sep))

        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep, quiet=quiet).items())
            if not v:  # empty dict
                items.append((new_key, v))
        else:
            items.append((new_key, v))
    return dict(items)


def nest_dict(d, sep='.'):
    """
    Transform flatted dict to nested dict.

    :param d: dict
    :param sep: separator string
    :return: nested dict
    :rtype: dict
    """
    ret = {}
    for k, v in d.items():
        if sep in k:
            keys = k.split(sep)
            target = ret

            while len(keys) > 1:
                current_key = keys.pop(0)
                target = target.setdefault(current_key, {})
            target[keys[0]] = v
        else:
            ret[k] = v
    return ret


class SuperDict(object):

    __slots__ = ('_settings', '_flat', '_sep')

    def __init__(self, data=None, sep='.', quiet=False):
        super().__init__()
        self._settings = data if isinstance(data, dict) else {}
        self._flat = flatten_dict(self._settings, sep=sep, quiet=quiet)
        self._sep = sep

    def get(self, key):
        """
        Get config by key, support dot(.) to search in objects.

        :param key: config key
        :return: object
        """
        if '.' in key:
            if key in self._flat:
                return self._flat[key]
        else:
            if key in self._settings:
                return self._settings[key]
        return None

    def set(self, key, value):
        """
        Set key with value in config, key also support dot(.) and will merge automatically.

        :param key: config key
        :param value: config value
        """
        self._flat[key] = value
        self._settings = nest_dict(self._flat, sep=self._sep)

    def as_dict(self):
        """
        Return dict object.

        :return: dict
        :rtype: dict
        """
        return self._settings

    def as_flatten_dict(self):
        """
        Return flattened dict object
        :return:
        :rtype:
        """

        return self._flat

    def merge(self, other):
        """
        Merge other SuperDict to this. This will union keys in this and other.
        All keys in other will replace existing keys in this.

        :param other: other SuperDict object
        :return: self
        :rtype: SuperDict
        """
        if not isinstance(other, SuperDict):
            raise TypeError('Not SuperDict type')
        new_dict = flatten_dict(other.as_dict(), sep=self._sep)
        self._flat.update(new_dict)
        self._settings = nest_dict(self._flat, sep=self._sep)
        return self

    def __str__(self, *args, **kwargs):
        return str(self._settings)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __contains__(self, item):
        if self._sep in item:
            return item in self._flat
        else:
            return item in self._settings

    def __iter__(self):
        for key in self._settings:
            yield key
