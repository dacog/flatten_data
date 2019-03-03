#function flatten_data is taken from https://github.com/thomascmann/flatten-data
#MIT License
#Copyright (c) 2017 Thomas C. Mann
#I just packaged this as I found it to be really useful when dealing with nested dictionaries and lists
import copy
from collections.abc import MutableMapping, MutableSequence

def flatten_data(data, simple=1):
    out = []

    def flatten(x, name='',subgroup=None):
        if subgroup is None:
            subgroup = [{}]
        if isinstance(x, MutableMapping):
            for a in x:
                subgroup = flatten(x[a], ''.join([name, str(a), "_"]), subgroup)
        elif isinstance(x, MutableSequence):
            new_dicts = []
            for a in x:
                for dic in subgroup:
                    newdict = flatten(a, name, copy.deepcopy([dic]))
                    for i in newdict:
                        new_dicts.append(i)
            subgroup = new_dicts   
        else:
            for dic in subgroup:
                dic[name[:-1]] = x
        return subgroup

    if simple == 1:
        formatted_data = flatten(data)
        for i in formatted_data:
            out.append(i)
    else:
        for record in data:
            if isinstance(data, MutableSequence):
                formatted_data = flatten(record)
            elif isinstance(data, MutableMapping):
                formatted_data = flatten(data[record])
                for i in formatted_data:
                    i["_ID_VAR_"] = record

            for i in formatted_data:
                out.append(i)
    return out
