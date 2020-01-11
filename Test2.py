
def find_depth(data, depth, key_list):
    if not data:
        return key_list
    
    for key, value in data.items():
        key_list.append('{} {}'.format(key, depth))

        if isinstance(value, (int, float, str)):
            pass
        elif isinstance(value, dict):
            return find_depth(value, depth+1, key_list)
        elif isinstance(value, object):
            if value is not None:
                return find_depth(value.__dict__, depth+1, key_list)

    return key_list

def print_depth(data):
    print(*find_depth(data, 1, []), sep='\n')


######### Test Start Here ################

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

b = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b
        }
    }
}

print_depth(b)