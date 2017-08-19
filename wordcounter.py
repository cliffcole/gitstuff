def isWhiteSpace(character):
    return character == ' '   or character == '\n'
    

def slice(sentance):
    words = []
    beginningOfWord = 0
    currentCharacter = 0

    for character in sentance:
        
        if isWhiteSpace(character):
            
            word = sentance[beginningOfWord:currentCharacter]
            words.append(word.lower())
            beginningOfWord = currentCharacter + 1
        elif currentCharacter == len(sentance) - 1:
            word = sentance[beginningOfWord:len(sentance)]
            words.append(word.lower())
            
        currentCharacter += 1
        
    return words

def countWords(sentance):
    wordCount = {}
    words = slice(sentance)
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    print wordCount 

countWords("HellO this is A SenTance hello")