class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a','e','i','o','u'}
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            if sentence[i][0].lower() not in vowels:
                sentence[i] = sentence[i][1:] + sentence[i][0]+'ma'+('a'*(i+1))
            else:
                sentence[i] = sentence[i]+'ma'+('a'*(i+1))
        sentence = ' '.join(word for word in sentence)
        return sentence