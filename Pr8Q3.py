#WAP to perform create, update, insert and delete function on hash table
hash_table = [[] for i in range(10)]
print(hash_table)

#insert data into hash table
def insert(hash_table,key,value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            key_exists == True
            break
    if key_exists:
        bucket[i] = ((key,value))
    else:
        bucket.append((key,value))

insert(hash_table,10, 'Nepal')
insert(hash_table,25,'USA')
insert(hash_table,20,'India')
print(hash_table)

#Search an element in hash table
def search(hash_table,key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            return v

print(search(hash_table, 10))
print(search(hash_table, 20))
print(search(hash_table, 30))

# delete an element from the hash table
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print("Key {} deleted".format(key))
    else:
        print('Key {} not found'.format(key))

delete(hash_table,10)
print(hash_table)
