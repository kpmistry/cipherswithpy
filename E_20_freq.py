#import getCanditatemap() from E_18_hacksub
import operator

ETAOIN = """ etaoinsrhldcumgyfpwb.,vk0-'x)(1j2:q"/5!?z346879%[]*=+|_;\>$#^&@<~{}`""" #order taken from https://mdickens.me/typing/theory-of-letter-frequency.html, with space added at the start
length = 128

def getCanditatemap():
        return (dict.fromkeys((chr(i) for i in range(length)),0)) # https://stackoverflow.com/questions/2241891/how-to-initialize-a-dict-with-keys-from-a-list-and-empty-value-in-python/2241904

def getLettercount(mess):
   
    charcount = getCanditatemap()
    for char in mess:
        if char in charcount:
            charcount[char] +=1

    return charcount

def getFreqOrder(mess):

    #get a dictionary of each letter and its frequency count
    lettertofreq = getLettercount(mess)
    
     # second, make a dictionary of each frequency count to each letter(s) with that frequency
    freqtochar = {}
    for i in range(length):
        i=ch(i)
        if lettertofreq[i] not in freqtochar: # look for frequencies not present
            freqtochar[lettertofreq[i]] = [i] # add if not present, else append
        else:
            freqtochar[lettertofreq[i]].append(i)

    #reverse ETAOIN order, for each list of letters (per frequency)
    for freq in freqtochar:
        freqtochar[freq].sort(key=ETAION.find, reverse=True)
        freqtochar[freq] = ''.join(freqtochar[freq]) # convert to string
    
    # sort them in order of frequency
    freqpairs = sorted(freqtochar.items(), key=operator.itemgetter(0), reverse=True)
    
    # extractst the values and joins them together
    freqorder = []
    values = freqpairs.values() # grabs the values only
    for freqpair in values:
        freqorder.append(freqpair)

    return ''.join(freqorder)

def englishFreqMatch(message):
    
    matchscore =0
    freqOrder = getFreqOrder(message.lower()) # convert to lower case as we are just looking for frequency match score, so case of the letter should not matter
    for commletter in (ETAION[:7] or ETAION[-7]):
        if commletter in freqOrder[:7]:
            matchscore +=1

    return matscore
