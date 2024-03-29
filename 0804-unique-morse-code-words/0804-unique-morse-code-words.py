class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new_word = ''
        new_list = []
        mySet = set()
        for word in words:
            for letter in word:
                if letter in alphabet:
                    letter_index = alphabet.index(letter)
                    new_word += morse[letter_index]
            mySet.add(new_word)
            new_word = ''
        return len(mySet)