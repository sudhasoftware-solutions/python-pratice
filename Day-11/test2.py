my_set = {1, 2, 3, 4, 5}

my_set.add(6)  # Adding an element
my_set.remove(3)  # Removing an element

print(my_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)  # Difference of sets

print (union_set,intersection_set,difference_set)

is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2

print(is_subset ,is_superset)

#####################################################

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

server_name = 'server1'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")