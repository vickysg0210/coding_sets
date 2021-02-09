class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)] #使用list数据结构作为哈希表元素保存方法
        self.count = size #最大表长
    def hash(self, key):
        return key % self.count #散列函数采用除留余数法
    def insert_hash(self, key, value):
        address = self.hash(key)
        while self.elem[address]:
            address = (address + 1) % self.count
        self.elem[address] = value

    def search_hash