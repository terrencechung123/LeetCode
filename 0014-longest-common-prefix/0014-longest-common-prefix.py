class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            target = strs[0][i]
            for w in strs:
                if i == len(w) or w[i] != target:
                    return res
            res += target
        return res