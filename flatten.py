def flatten(thing,sep='_'):
    result = {}
    stack = [{"thing": thing, "path": ""}]
    while stack:
        current = stack.pop()
        if type(current["thing"]) is dict:

            for new_key,new_thing in current["thing"].items():
                stack.append({
                    "thing" : new_thing,
                    "path" : current["path"] +(sep if current["path"] else '')+new_key
                })
        
        elif type(current["thing"]) is list:

            for i,new_thing in enumerate(current["thing"]):
                stack.append({
                    "thing":new_thing,
                    "path" : current["path"]+sep+str(i)
                })
        
        else:
            result[current["path"]] = current["thing"]

    return result
def flatten_rec(thing, key_so_far:str='',curr_key:str='', 
    sep:str='_', result:dict={}) -> dict:
    
    #append curr_key to key_so_far except at the beginning
    key_so_far = key_so_far+sep+curr_key if key_so_far else curr_key
    
    if type(thing) is dict:
        # if its a dictionary
        # 1. pass the new_key to be appended to key_so_far
        # 2. pass new_thing to be treated by flatten as required
        for new_key, new_thing in thing.items():
            flatten(new_thing, key_so_far, new_key, sep, result)
            
        # if its an array, simply call flatten for each of its elements
    elif type(thing) is list:
        for new_thing in thing:
            flatten(new_thing, key_so_far, str(i), sep, result)
    else:
        final_key = key_so_far #we have reached a simple key,value pair
        result[final_key] = thing
        
    return result


if __name__ == "__main__":
    pass
 




