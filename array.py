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
                        for x in range(self.size, i, -1):    # 从最后一个元素开始后移
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
                for x in range(i, self.size):    # 从i开始所有元素后移
                    if x + 1 == self.size:    # 边界处理
                        self.data[x] = None
                    else:
                        self.data[x] = self.data[x + 1]
                self.size -= 1
                break


def test_SortedArray():
    a_list = [9, 1, 2, 7, 8, 6, 5, 10, 4, 3]
    d_list = [5, 1, 8, 0]
    sortedArray = SortedArray()
    for v in a_list:
        sortedArray.add(v)
    print('size:', sortedArray.size)
    print(sortedArray.data)
    for v in d_list:
        sortedArray.remove(v)
    print('size:', sortedArray.size)
    print(sortedArray.data)

def test():
    for x in range(0, 10):
        print(x)


if __name__ == '__main__':
    test_SortedArray()
    # test()
