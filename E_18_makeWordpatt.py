# Makes the wordPatterns.py File

# Creates wordPatterns.py based on the words in our dictionary text file, dictionary.txt.

import pprint, E_12_English_detect


def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    '''
    if (isinstance(word, basestring)):#checks if the word is a string and if so converts to upper case
           word = word.upper() # need to user upper as the dictionary we are using is all upper case, can remove if not needed
    '''
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        ascii_val = ord(letter)
        if ascii_val not in letterNums:
            letterNums[ascii_val] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[ascii_val])
    return '.'.join(wordPattern)


def main():
    allPatterns = {}

    wordList = E_12_English_detect.readfilesplit("dictionary.txt")

    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement.
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    main()
