# -*- coding:utf-8 -*-
from itertools import islice
import os
import re

userDictPath = 'data/'
wholeUserDict = 'allwords.txt'


def mergeDict():
    items = set()
    dictFiles = []
    for (dirpath, dirnames, filenames) in os.walk(userDictPath):
        dictFiles.extend(filenames)
        break
    for dict in dictFiles:
        wordList = []
        dict = userDictPath + dict
        with open(dict, 'r', encoding='utf-8') as fin:
            for line in islice(fin, 0, None):
                line = line.strip('\n')
                isTitle = re.match('^[a-zA-Z]+.?\t.+.?\t.*', line)
                if isTitle is not None:
                    print(line)
                    continue
                isMatch = re.match('^[0-9]+.?\t.*', line)
                if isMatch is not None:
                    line = re.sub('^[0-9]+.?\t', '', line)
                isWord = re.match('^[a-zA-Z- \'éàèâêûôœüßäö]+.?\t.*', line)
                if isWord is not None:
                    items.add(line)
                    wordList.append(line)
                else:
                    print(line)

        with open(dict, 'w', encoding='utf-8') as fout:
            for word in wordList:
                fout.write(word + '\n')

    wordlist = sorted(items)
    with open(wholeUserDict, "w") as fout:
        fout.write("")
    with open(wholeUserDict, "a", encoding='utf-8') as fout:
        for word in wordlist:
            fout.write(word + "\n")

if __name__ == "__main__":
    mergeDict()