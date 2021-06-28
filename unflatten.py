
def find_list_sizes(d, sep='_'):
    list_sizes = {}
    for x in d.keys():
        splitted = x.split(sep)
        for i, possible_idx in enumerate(splitted[1:]):
            if not possible_idx.isdigit():
                continue
            prev = splitted[i]
            if prev not in list_sizes:
                list_sizes[int(prev) if prev.isdigit()
                           else prev] = int(possible_idx)+1
            else:
                if int(possible_idx) > list_sizes[int(prev) if prev.isdigit() else prev]:
                    list_sizes[int(prev) if prev.isdigit()
                               else prev] = int(possible_idx)+1
    return list_sizes


def _helper_nest_dict(key_curr_level, value, subresult, list_sizes, sep='_', list_flag=False):

    key_curr_level, *rest = key_curr_level.split('_', 1)
    idx_or_key = int(key_curr_level) if list_flag else key_curr_level

    if rest and key_curr_level:

        key_next_level, *rest_next = rest[0].split('_', 1)
        # if the next level has a key which is a digit, then treat is as a list and pass
        # a list container to the
        if key_next_level.isdigit():
            if (not list_flag and key_curr_level not in subresult) or (list_flag and subresult[int(key_curr_level)] == None):
                subresult[idx_or_key] = list_sizes[idx_or_key]*[None]
            _helper_nest_dict(
                rest[0], value, subresult[idx_or_key], list_sizes, list_flag=True)

        else:
            if (not list_flag and key_curr_level not in subresult) or (list_flag and subresult[int(key_curr_level)] == None):
                subresult[idx_or_key] = {}
            _helper_nest_dict(
                rest[0], value, subresult[idx_or_key], list_sizes)

    else:
        if key_curr_level:
            subresult[idx_or_key] = value


def unflatten(d, sep='_'):
    result = {}
    list_sizes = find_list_sizes(d, sep)
    for key, val in d.items():
        _helper_nest_dict(key, val, result, list_sizes, sep=sep)
    return result


if __name__ == "__main__":
    pass
