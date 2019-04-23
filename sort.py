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
        """插入排序，选第1个元素作为已排序的，从未排序区中选元素与已排序区元素比较，
        如果当前元素大于已排序区元素，则已排序区元素后移
        将当前元素插入到找到的位置
        """
        length = len(inputs)
        for i in range(1, length):
            for j in range(i, 0, -1):
                # 如果比前面的元素小，则往前移动
                if inputs[j] < inputs[j - 1]:
                    inputs[j - 1], inputs[j] = inputs[j], inputs[j - 1]
        return inputs

    def insert_sort2(self, inputs):
        length = len(inputs)
        for i in range(1, length):
            current = inputs[i]
            j = i - 1
            while j >= 0 and inputs[j] > current:
                inputs[j + 1] = inputs[j]
                j -= 1
            inputs[j + 1] = current
        return inputs

    def select_sort(self, inputs):
        """
        选择排序思路：分已排序区间和未排序区间，每次从未排序区间找到最小值，将其放入到已排序期间末尾
        """
        length = len(inputs)
        for i in range(length):
            # 找出最小值的序号
            min_index = i
            for j in range(i + 1, length):
                if inputs[j] < inputs[min_index]:
                    min_index = j
            # 交换
            tmp = inputs[i]
            inputs[i] = inputs[min_index]
            inputs[min_index] = tmp
        return inputs


if __name__ == '__main__':
    sort = Sort()
    inputs = [6, 5, 4, 3, 2, 1]
    print(inputs)
    # sorted_list = sort.bubble_sort(inputs)
    # sorted_list = sort.insert_sort2(inputs)
    sorted_list = sort.select_sort(inputs)
    print(sorted_list)
