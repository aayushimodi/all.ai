import re


sentence = "Woah that was insane! Did you see that crazy play!?"
words = re.findall(r"[\w']+|[.,!?;]", sentence)
d = {'insane': 'amazing', 'crazy': 'awesome'}



# def readFile():
#     f = open("text file path", r)
#     f.readline
#     f.close

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

lws = replaceTerms(words, d)
print(listToSentence(lws))