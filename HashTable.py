# Explaination


# A hashtable is sstructure that holds pairs (key,value)
# You can get value by key from hashtable

# There are different implementations of hashtables
# In that example hashtable consists of "buckets"
    # bucket = [('key1',1),('key2',2)]
    # Buckets can be any datastructure, for example binary tree
    # but in that implementation it is just a list

# When we want to append a new pair we must:
    # 1. calculate numeric hash of key:
        # in python you can use hash()
    # 2. mod numeric hash with the number of buckets in hashtable:
        # numeric_hash % number_of_buckets
        # result from operation 2. is index of the bucket
    # append new pair to bucket with index we got from 2.

# can be implemented any hash function that returns int number
HASHFUNCTION = hash

class HashTable:
    def __init__(self,max_buckets=1000):
        # in that implementation we are creating easy hashtable
        # with static number of buckets

        self.buckets = [[] for i in range(max_buckets)]

    def __setitem__(self,key,value):
        # sets pair (key,value)

        hash = HASHFUNCTION(key)
        bucket_index = hash % len(self.buckets)

        # The simpliest searching algorithm
        for pair in self.buckets[bucket_index]:
            pair_key = pair[0]
            if pair_key == key:
                pair[1] = value
                return

        # set value
        self.buckets[bucket_index].append([key,value])

    def __getitem__(self,key):
        # gets pair (key,value)

        hash = HASHFUNCTION(key)
        bucket_index = hash % len(self.buckets)

        for pair in self.buckets[bucket_index]:
            pair_key = pair[0]
            if pair_key == key:
                # returns value
                return pair[1]

        raise KeyError(f'There is no such key:{key} in hashtable')

    def __str__(self):
        str_hashtable = '{'

        for bucket in self.buckets:
            for pair in bucket:
                key = pair[0]
                value = pair[1]
                str_hashtable += f'{repr(key)}:{value}'
        
        str_hashtable += '}'
        return str_hashtable

    def __repr__(self):
        return str(self)







if __name__ == '__main__':
    ht = HashTable()
    ht['123'] = 5
    value = ht['123']
    print(value)
    print(ht)