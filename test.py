import flatten,unflatten
import json
import os
import pprint
def check_raw():
    schema = {
            "a": 1,
            "b": 2,
            "c": {
                "c1": [
                    [
                    {
                        "c11": 1,
                        "c12": 2,
                        "c13": 3
                    }],
                    {
                        "c21": 1,
                        "c22": 2,
                        "c23": 3
                    }
                ],
                "d1": [
                    {
                        "d11": 1,
                        "d12": 2,
                        "d13": 3
                    },
                    {
                        "d21": 1,
                        "d22": 2,
                        "d23": 3
                    },
                    1,
                    2,
                    "test"
                ]
            },
            "x": 1,
            "y": 2
        }


    flat = flatten.flatten(schema)
    print("FLAT")
    pprint.pprint(flat)
    nested = unflatten.unflatten(flat)
    print("NESTED")
    pprint.pprint(nested)

    print(nested == schema)

def flatten_json(json_file):
    
    d = {}
    with open(json_file) as f:
        d = json.load(f)
    d = flatten.flatten(d)
    json_string = json.dumps(d,sort_keys=True, indent=4)

    write_file = f"flattened_{json_file.rsplit('.',1)[0]}.json"
    if os.path.isfile(write_file):
        return f"File {write_file} already exists. Abort"
    with open(write_file, "w") as f:
        f.write(json_string)

#see ./unflatten.py for certain caveats regarding unflattening
def unflatten_json(json_file):
    # TODO put checks here as to whether or not param: json_file is actually flattened 
    d = {}
    with open(json_file) as f:
        d = json.load(f)
    
    d = unflatten.unflatten(d)
    json_string = json.dumps(d, sort_keys= True, indent = 4)

    write_file = f"unflattened_{json_file.rsplit('.',1)[0]}.json"
    if os.path.isfile(write_file):
        return f"File {write_file} already exists. Abort"
    with open(write_file, "w") as f:
        f.write(json_string)

        
        
check_raw()

flatten_json("response.json")
unflatten_json("flattened_response.json")

