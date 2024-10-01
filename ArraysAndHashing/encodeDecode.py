class Solution:
    def encode(self, strs) -> str:
        result_str = ""
        for s in strs:
            result_str += str(len(s)) + "$" + s
        return result_str

    def decode(self, s: str):
        res, i = [], 0
        while i < len (s):
            curr_word_len = int(s[i])
            i += 2
            res.append(s[i:i+curr_word_len])
            i += curr_word_len
        return res


solution = Solution()
encoded = solution.encode(["Hello","World","!!"])
print(encoded)
print(solution.decode(encoded))