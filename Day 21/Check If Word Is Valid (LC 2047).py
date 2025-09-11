class Solution:
    def countValidWords(self, sentence: str) -> int:
        sList = sentence.split()
        count = 0
        inc = True
        noPunt = 0
        noHyphen = 0
        for word in sList:
            for letter in word:
                if letter.isdigit():
                    inc = False
                    break
                if letter in ['!', '.', ',']:
                    noPunt += 1
                    if noPunt > 1 or letter != word[-1]:
                        inc = False
                        break
                if letter == '-':
                    noHyphen += 1
                    if noHyphen > 1:
                        inc = False
                        break
                    hyphenIndex = word.index('-')
                    if hyphenIndex == 0 or hyphenIndex == len(word) - 1 or not (word[hyphenIndex - 1].isalpha() and word[hyphenIndex + 1].isalpha()):
                        inc = False
                        break
                
            if inc:
                count += 1
            noPunt = 0
            noHyphen = 0
            inc = True
        return count