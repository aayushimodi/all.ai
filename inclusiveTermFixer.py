import re

# def readFile():
#     text = ""
#     f = open("input.txt", "r")
#     if(f.readable()):
#         text = f.read()
#     f.close()
#     return text

# def writeFile(output):
#     f = open("output.txt", "w")
#     f.write(output)
#     f.close

def createDict():
    d = {}
    f = open('dictionary.txt', 'r')
    for line in f:
        x = [elt.strip() for elt in line.split("=")]
        badWord = x[0]
        goodWord = x[1]
        d[badWord] = goodWord
    f.close()
    return d


def equalsPunc(c):
    if c == "." or c == "!" or c == "?" or c == "," or c == ":" or c == ";":
        return True
    else:
        return False

def listToSentence (lws):
    sentence = ""
    for i, w in enumerate(lws):
        sentence += w
        if i < len(lws) - 1:
            if not equalsPunc(lws[i+1]):
                sentence += " "
    return sentence

def replaceTerms (words,d):
    badWords = d.keys()
    for i, w in enumerate(words):
        for term in badWords:
            if (w == term):
                words[i] = d.get(term)
    return words

words = re.findall(r"[\w']+|[.,!?;&-]", INPUT)
d = createDict()
lws = replaceTerms(words, d)
output = listToSentence(lws)
