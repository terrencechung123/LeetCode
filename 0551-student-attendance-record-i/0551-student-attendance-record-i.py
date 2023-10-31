class Solution:
    def checkRecord(self, s: str) -> bool:
        my_dict = {'A': 0, 'L': 0}
        for i in range(len(s)):
            if s[i] in my_dict:
                if my_dict[s[i]]>=2:
                    return False
                if s[i] == 'A':
                    my_dict[s[i]] += 1
                if s[i] == 'L':
                    if i > 0 and s[i] == s[i-1]:
                        my_dict[s[i]]+=1
                    else:
                        my_dict[s[i]]=0
        for x,y in my_dict.items():
            if y >= 2:
                return False
        return True