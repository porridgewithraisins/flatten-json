# flatten-json
Flatten a nested JSON file , and also unflatten it, in python

## Usage
```py
import flatten
d = {}
with open(json_file) as f:
    d = json.load(f)
d = flatten.flatten(d, sep = '->') # sep = '_' by default. This is the delimiter for nesting
# a : { b : c } will become a->b->c
json_string = json.dumps(d,sort_keys=True, indent=4)

import unflatten
d = {}
with open(flattened_json_file) as f:
    d = json.load(f)

d = unflatten.unflatten(d, sep = '->') # sep needs to be what separates nesting in the file
# sep = '_' by default
json_string = json.dumps(d, sort_keys= True, indent = 4)
```
    
