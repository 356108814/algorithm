class Solution:
    def reverseWords(self, s: str) -> str:
        r = ''
        a = s.split(' ')
        length = len(a)
        first = False
        for i in range(length - 1, -1, -1):
            word = self.trim(a[i])
            if len(word) > 0:
                if r != '':
                    r += ' '
                r += word
        return r

    def trim(self, s: str) -> str:
        r = ''
        length = len(s)
        for i in range(length):
            char = s[i]
            if char == ' ':
                continue
            r += char
        return r

    def reverse(self, s: str) -> str:
        r = ''
        length = len(s)
        has_blank = False
        for i in range(length, -1, -1):
            char = s[i]
            if char == ' ':
                if has_blank:
                    continue
                else:
                    has_blank = True
                    r += char
            else:
                r += char
                has_blank = False
            print(char)
        return r


if __name__ == '__main__':
    solution = Solution()
    s1 = "the sky is blue"
    s2 = "  hello world!  "
    s3 = "a good   example"
    s4 = "example  "
    print(solution.reverseWords(s3))
# print(solution.trim(s4))
