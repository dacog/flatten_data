# flatten-data

I found a great function from Thomas C. Mann at [https://github.com/thomascmann/flatten-data
]()
**In his words**
>Python script for flattening nested data into a list of dicts, designed for importing into a pandas DataFrame.
>The script takes a nested data object and returns a list of dicts. Dicts within the object are flattened, and lists within the object are converted into separate dicts within the returned outer list, copying higher-level elements

## Install

On Jupyter Notebooks use

```python 
!pip install git+https://github.com/dacog/flatten_data
```
On normal pip use

```python
pip install git+https://github.com/dacog/flatten_data
```

## Import
```python
from flatten_data import flatten_data as fd
```

## Use

```python
fd.flatten_data(data, simple=0)
```

_simple_ can have a value of 0 or 1. Check the examples to learn more.
