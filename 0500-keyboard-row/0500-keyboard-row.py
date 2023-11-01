class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top_row = 'qwertyuiop'
        mid_row = 'asdfghjkl'
        bottom_row = 'zxcvbnm'
        result = []
        for word in words:
            myDict = {'not_top':False,'not_mid':False,'not_bottom':False}
            for letter in word:
                if letter.lower() not in top_row:
                    myDict['not_top'] = True
                if letter.lower() not in mid_row:
                    myDict['not_mid'] = True
                if letter.lower() not in bottom_row:
                    myDict['not_bottom'] = True
            for i in myDict:
                if myDict[i] == False:
                    result.append(word)
        return result