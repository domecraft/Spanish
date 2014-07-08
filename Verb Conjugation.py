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
    verb = raw_input("Enter the infinitive of the verb: ")
    try:
        int(word)
    except:
        inputwCorrect = True
        
verbRoot = verb[:len(verb) - 2:]
verbEnding = verb[len(verb) - 2:]

print verbEnding

if pronoun == "yo":
    conjugatedVerb = verbRoot + "o"
elif pronoun == "tu":
    if (verbEnding == "er") or (verbEnding == "ir"):
        conjugatedVerb = verbRoot + "es"
    else:
        conjugatedVerb = verbRoot + "as"
elif pronoun == "usted"
    if (verbEnding == "er") or (verbEnding == "ir"):
        conjugatedVerb = verbRoot + "e"
    else:
        conjugatedVerb = verbRoot + "a"




    
print
print "The verb conjugated is: " + conjugatedVerb

    

    
