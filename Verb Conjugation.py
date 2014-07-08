inputpCorrect = False
while inputpCorrect == False:
    print 
    pronoun = raw_input("Enter a pronoun: ")
    try:
        int(pronoun)
    except:
        inputpCorrect = True
    print 
inputwCorrect = False
while inputwCorrect == False:
    print
    word = raw_input("Enter a word: ")
    try:
        int(word)
    except:
        inputwCorrect = True
        
wordRoot = word[:len(word) - 2:]
wordEnding = word[len(word) - 2:]
