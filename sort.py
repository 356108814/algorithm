# coding: utf-8


class Sort(object):
    """各种排序"""

    def bubble_sort(self, inputs):
        """冒泡排序，每轮两两比较相邻的2个元素，若顺序不对，则交换"""
        length = len(inputs)
        for i in range(length):
            for j in range(length - i - 1):
                if inputs[j] > inputs[j + 1]:
                    tmp = inputs[j + 1]
                    inputs[j + 1] = inputs[j]
                    inputs[j] = tmp
        return inputs

    def insert_sort(self, inputs):
        """插入排序，选第1个元素作为已排序的，"""
        length = len(inputs)
        for i in range(1, length):
            for j in range(i, 0, -1):
                # 如果比前面的元素小，则往前移动
                if inputs[j] < inputs[j - 1]:
                    inputs[j - 1], inputs[j] = inputs[j], inputs[j - 1]
        return inputs


if __name__ == '__main__':
    sort = Sort()
    inputs = [6, 5, 4, 3, 2, 1]
    print(inputs)
    # sorted_list = sort.bubble_sort(inputs)
    sorted_list = sort.insert_sort(inputs)
    print(sorted_list)
