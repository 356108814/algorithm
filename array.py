# encoding: utf-8

class Array(object):
    """
    动态扩容的数组
    """
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, value):
        length = len(self.data)
        is_full = self.data[length - 1] is not None # 判断是否已满
        if is_full:
            tmp = [None] * length * 2
            for i, v in enumerate(self.data):
                tmp[i] = v
            self.data = tmp
        for i, v in enumerate(self.data):
            if v is None:
                self.data[i] = value
                break
    
    def remove(self, value):
        for i, v in enumerate(self.data):
            if v == value:
                self.data[i] = None
                break
                
    def printf(self):
        print(self.data)
        
    

if __name__ == '__main__':
    a = Array()
    a.printf()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.add(6)
    a.add(7)
    a.add(8)
    a.add(9)
    a.add(10)
    a.printf()
    a.add(11)
    a.printf()
    a.add(12)
    a.printf()
    a.remove(7)
    a.printf()
