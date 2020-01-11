
# Find Depth of dict
def find_depth(data, depth, key_list):
    if not data:
        return key_list
    
    for key, value in data.items():
        key_list.append('{} {}'.format(key, depth))
        
        if isinstance(value, dict):
            return find_depth(value, depth+1, key_list)

    return key_list

# Print dict
def print_depth(data):
    print(*find_depth(data, 1, []), sep='\n')


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}
print_depth(a)