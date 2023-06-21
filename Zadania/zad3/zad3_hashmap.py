def hash(key, n):
    ret = 0

    prime1 = 17
    prime2 = 663564636797 # podobno prime
    power = 1

    for letter in key:
        ret = (ret + (ord(letter)) * power) % prime2
        power = (power * prime1) % prime2
    
    return ret % n

class HashMapCount():
    def __init__(self, n):
        self.n = n
        self.map = [[] for _ in range(n)]

    def add(self, key):
        map = self.map
        hash_key = hash(key, self.n)

        if map[hash_key] == []:
            map[hash_key].append([key, 1])
        else:
            for elem in map[hash_key]:
                if elem[0] == key:
                    elem[1] += 1
                    map[hash_key][0] = max(map[hash_key][0], elem[1])
            map[hash_key].append([key, 1])

    def get_max(self):
        map = self.map
        ret = 0
        for container in map:
            ret = max(ret, container)

        return ret

def strong_string(T):
    hashmap = HashMapCount(len(T))

    for word in T:
        hashmap.add(word)
        if word != word[::-1]:
            hashmap.add(word[::-1])

    return hashmap.get_max()