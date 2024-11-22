# super-dict

SuperDict object is a wrapper for dict that restrict some functionality.
It only supports multiple level keys and can use dot (.) to get inner value.
For the first level, type for values can only be: dict, list, string, number, bool and None.
From the second level, list can only be the last level. 

---

## Contents
<!-- TOC -->
* [super-dict](#super-dict)
  * [Contents](#contents)
  * [Examples](#examples)
    * [structure data](#structure-data)
    * [Operations](#operations)
      * [GET](#get)
      * [SET](#set)
      * [MERGE](#merge)
      * [Loop](#loop)
      * [IN](#in)
    * [custom separator](#custom-separator)
    * [NOTICE](#notice)
  * [Tests](#tests)
  * [Support](#support)
<!-- TOC -->

---

## Examples
Example Data
```python
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

```
### structure data
```doctest
>>> data = SuperDict(dictA)
>>> print(type(data))
<class 'super_dict.structure_data.SuperDict'>

>>> print(data)
{'key1': 'value1', 'key2': {'key2-1': 'value2-1'}, 'key3': {'key3-1': {'key3-1-1': [1, 2, 3, 4, 5], 'key3-1-2': 3, 'key3-1-3': None}}}

>>> print(data.as_flatten_dict())
{'key1': 'value1', 'key2.key2-1': 'value2-1', 'key3.key3-1.key3-1-1': [1, 2, 3, 4, 5], 'key3.key3-1.key3-1-2': 3, 'key3.key3-1.key3-1-3': None}

>>> print(data.as_dict())
{'key1': 'value1', 'key2': {'key2-1': 'value2-1'}, 'key3': {'key3-1': {'key3-1-1': [1, 2, 3, 4, 5], 'key3-1-2': 3, 'key3-1-3': None}}}

```

### Operations
#### GET
```doctest
>>> data = SuperDict(dictA)
>>> print(data.get('key1'))
value1

>>> print(data.get('key2.key2-1'))
value2-1

>>> print(data.get('key3.key3-1.key3-1-1'))
[1, 2, 3, 4, 5]

>>> print(data.get('key3.key3-1.key3-1-2'))
3

>>> print(data.get('key3.key3-1.key3-1-3'))
None

```

#### SET
```doctest
>>> data = SuperDict(dictA)
>>> key = 'key3.key3-1.key3-1-2'
>>> print(f"before: {data.get(key)}")
before: 3
>>> data.set(key, 4)
>>> print(f"after: {data.get(key)}")
after: 4

```

#### MERGE
```doctest
>>> data = SuperDict(dictA)
>>> key = 'key3.key3-1.key3-1-2'
>>> print(f"before merge: {data.get(key)}")
before merge: 3

>>> data = data.merge(SuperDict(dictB))
>>> print(f"after merge: {data.get(key)}")
after merge: 4

```

#### Loop

```doctest
>>> data = SuperDict(dictA)

>>> for key in data:
...    print(key)
key1
key2
key3

>>> for key in data.as_flatten_dict():
...    print(key)
key1
key2.key2-1
key3.key3-1.key3-1-1
key3.key3-1.key3-1-2
key3.key3-1.key3-1-3

```

#### IN
```doctest
>>> data = SuperDict(dictA)
>>> print('key1' in data.as_flatten_dict())
True
>>> print('key3.key3-1.key3-1-1' in data.as_flatten_dict())
True

```

### custom separator
```doctest
>>> data = SuperDict(dictC, sep='#')
>>> print(data.as_flatten_dict())
{'key#dot.key': 2}

```

### NOTICE
list can ONLY be the last level!
```doctest

>>> data = SuperDict(dictD)
>>> print(data)
{'key': {'key-1': [{'key-1-list-1': 1}, {'key-2-list-2': [1, 2, 3, 4]}]}}
>>> print(data.as_flatten_dict())
{'key.key-1': [{'key-1-list-1': 1}, {'key-2-list-2': [1, 2, 3, 4]}]}

```

---

## Tests
```shell

make test

```
---

## Support
If you have questions, feel free to reach out to [liozza@163.com].