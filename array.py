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


class SortedArray(object):
    """大小固定的有序数组（升序），支持动态增删操作"""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def add(self, value):
        if self.size == self.capacity:
            print('数组已满')
        else:
            for i, v in enumerate(self.data):
                if v is None:
                    self.data[i] = value
                    self.size += 1
                    break
                else:
                    if value <= v:    # 确定了插入的位置
                        for x in range(self.size, i, -1):    # 元素后移
                            self.data[x] = self.data[x-1]
                        self.data[i] = value
                        self.size += 1
                        break
                    else:
                        continue
        

    def remove(self, value):
        for i, v in enumerate(self.data):
            if v == value:    # 找到元素位置
                self.data[i] = None
                for x in range(i + 1, self.size):    # 元素后移
                    self.data[x] = self.data[x+1]
                self.size -= 1

        pass
        

def test_SortedArray():
    tmp = [9, 1, 2, 7, 8, 6, 5, 10, 4, 3]
    # tmp = [9, 1, 2, 7]
    sortedArray = SortedArray()
    for v in tmp:
        sortedArray.add(v)
        print('size:', sortedArray.size)
        print(sortedArray.data)

if __name__ == '__main__':
    test_SortedArray()
