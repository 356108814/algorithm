# coding: utf-8
import math
from typing import List


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
                inputs[j + 1] = inputs[j]  # 已排序的后移l
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

    def merge_sort(self, inputs):
        """
        归并排序
        """
        length = len(inputs)
        if length == 1:  # 不能再分了，直接返回，否则死循环
            return inputs
        mid = math.floor(length / 2)
        left = self.merge_sort(inputs[0: mid])
        right = self.merge_sort(inputs[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """合并2个数组合并为一个有序的数组"""
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 将未比较处理的数据加入数组末尾
        result += left[i:]
        result += right[j:]
        return result

    def quick_sort(self, inputs: List[int]):
        """快速排序"""
        return self.quick_sort_c(inputs, 0, len(inputs) - 1)

    def quick_sort_c(self, inputs: List[int], low: int, high: int):
        """
        递归排序
        :param inputs:
        :param low: 最小下标
        :param high: 最大下标
        :return:
        """
        if low < high:
            m = self.partition(inputs, low, high)
            self.quick_sort_c(inputs, low, m - 1)
            self.quick_sort_c(inputs, m + 1, high)
        return inputs

    def partition(self, inputs: List[int], low: int, high: int):
        """快排分区函数，为了使快排是原地排序算法，空间复杂度为O(1)"""
        pivot, j = inputs[low], low
        for i in range(low + 1, high + 1):
            if inputs[i] <= pivot:
                j += 1
                inputs[j], inputs[i] = inputs[i], inputs[j]
        inputs[low], inputs[j] = inputs[j], inputs[low]
        return j

    def quick_sort2(self, inputs: List[int], left: int, right: int):
        if left >= right:
            return inputs
        pivot = inputs[left]
        low = left
        high = right
        while left < right:
            while left < right and inputs[right] >= pivot:
                right -= 1
            inputs[left] = inputs[right]
            while left < right and inputs[left] <= pivot:
                left += 1
            inputs[right] = inputs[left]
        inputs[right] = pivot
        self.quick_sort2(inputs, low, left - 1)
        self.quick_sort2(inputs, left + 1, high)
        return inputs


if __name__ == '__main__':
    sort = Sort()
    inputs = [6, 5, 4, 3, 2, 1]
    print(inputs)
    # sorted_list = sort.bubble_sort(inputs)
    # sorted_list = sort.insert_sort2(inputs)
    # sorted_list = sort.select_sort(inputs)
    sorted_list = sort.quick_sort(inputs)
    sorted_list = sort.quick_sort2(inputs, 0, len(inputs) - 1)
    print(sorted_list)
