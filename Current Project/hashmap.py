'Hashmap ADT'
class HashMap:
    'Makes a hashmap dictionary'
    def __init__ (self):
        'init hashmap'
        self.buckets = 100
        self.size1 = 0
        self.hash_table = [[] for i in range(self.buckets)]

    def get(self, key):
        'gets value in dict'
        rc_key = int(str(key[0])+str(key[1]))

        #Better but broken hashing function
        # x = key[0]
        # y = key[1]
        # n = x-2
        # rc_key = (int(2*x+y+(0.5*n*(n+1)))-1)

        if rc_key > self.buckets:
            raise(KeyError)
        elif(self.hash_table[rc_key] == []):
            raise(KeyError)
        else:
            bucket = self.hash_table[rc_key]
            return bucket [1]

    def set(self, key, value):
        'inserts value into hashmap'
        # Broken code that breaks pylint
        # global first_time
        # self.size1 +=1
        # if first_time == 1:
        #     self.buckets = 100
        #     self.hash_table = [[] for i in range(self.buckets)]
        #     first_time = 0


        rc_key = int(str(key[0])+str(key[1]))

        #Better Hashing funct
        # x = key[0]
        # y = key[1]
        # n = x-2
        # rc_key = (int(2*x+y+(0.5*n*(n+1)))-1)
        # print(rc_key)


        self.hash_table[rc_key] = [rc_key,value]

        print(self.hash_table)

        # if (self.size1/self.buckets) >= .8:
        #     temp_num = self.buckets
        #     self.buckets = ((2*self.buckets)-1)
        #     print(self.buckets)
        #     print(temp_num)
        #     print(range(temp_num, self.buckets))
        #     for i in range(temp_num, self.buckets):
        #         self.hash_table.append([] )

    def remove(self, key):
        'removes value from dict'
        pass

    def clear(self):
        'clears entire bucket'
        self.buckets = 7
        self.size1 = 0
        self.hash_table = [[] for i in range(self.buckets)]

    def capacity(self):
        'returns the size of the bucket'
        return self.buckets

    def size(self):
        'returns the size of dict'
        return self.size1

    def keys(self):
        'returns list of keys'
        temp = []
        for i in range(self.buckets):
            if self.hash_table[i] != []:
                vals = self.hash_table[i]
                final_val = vals[0]
                final_val /= 11
                temp.append((int(final_val),int(final_val)))
        return temp
