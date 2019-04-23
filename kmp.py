# coding: utf-8


class KMP(object):
    """
    KMP算法，给定一个字符串s，查找模式串p在字符串s中的起始位置，找不到返回-1
    """

    def index(self, s, p):
        """暴力匹配"""
        s_len = len(s)
        p_len = len(p)
        i = 0
        j = 0
        while i < s_len and j < p_len:
            if s[i] == p[j]:    # 匹配成功，继续匹配下一个字符
                i += 1
                j += 1
            else:
                i = i - j + 1   # 匹配失败，i回溯，j置0，重新开始匹配？为什么要回去？
                j = 0
        if j == p_len:  # 匹配完成
            return i - j
        else:
            return -1

    def index2(self, s, p):
        """KMP"""
        s_len = len(s)
        p_len = len(p)
        next_array = self.get_next_array(p)
        i = 0
        j = 0
        while i < s_len and j < p_len:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                # 表示j对应的next值
                j = next_array[j]
        if j == p_len:  # 匹配完成
            return i - j
        else:
            return -1

    def get_next_array(self, p):
        # next_array第0位默认为-1
        next_array = [-1]
        p_len = len(p)
        k = -1
        j = 0
        while j < p_len - 1:
            # p[k]表示前缀，p[j]表示后缀
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                next_array.insert(j, k)
            else:
                k = next_array[k]
        return next_array


if __name__ == '__main__':
    s = 'abcasdfasdfdgdsgdsgsdfg'
    p = 'fdgd'
    kmp = KMP()
    index = kmp.index(s, p)
    # index2 = s.find(p)
    index2 = kmp.index2(s, p)
    print(index)
    print(index2)
