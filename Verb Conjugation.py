inputtCorrect = False
while inputtCorrect == False:
    tense = raw_input("Enter the tense of the verb (present or future):")
    tense = tense.lower()
    try:
        int(tense)
    except:
        inputtCorrect = True
    print
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

if tense == "present":
    if pronoun == "yo":
        conjugatedVerb = verbRoot + "o"
    elif pronoun == "tu":
        if (verbEnding == "er") or (verbEnding == "ir"):
            conjugatedVerb = verbRoot + "es"
        else:
            conjugatedVerb = verbRoot + "as"
    elif (pronoun == "usted") or (pronoun == "ella") or (pronoun == "el"):
        if (verbEnding == "er") or (verbEnding == "ir"):
            conjugatedVerb = verbRoot + "e"
        else:
            conjugatedVerb = verbRoot + "a"
    elif (pronoun == "ellas") or (pronoun == "ellos") or (pronoun == "ustedes"):
        if (verbEnding == "er") or (verbEnding == "ir"):
            conjugatedVerb = verbRoot + "en"
        else:
            conjugatedVerb = verbRoot + "an"
    elif (pronoun == "nosotros") or (pronoun == "nosotras"):
        if (verbEnding == "er") or (verbEnding == "ir"):
            conjugatedVerb = verbRoot + "imos"
        else:   
            conjugatedVerb = verbRoot + "amos"
            
if tense == "past imperfect":
    if pronoun == "yo":
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ía"
        else:
            conjugatedVerb = verbRoot + "aba"
    if pronoun == "tu":
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ías"
        else:
            conjugatedVerb = verbRoot + "abas"
    if (pronoun == "usted") or (pronoun == "el") or (pronoun == "ella"):
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ía"
        else:
            conjugatedVerb = verbRoot + "aba"
    if (pronoun == "ellos") or (pronoun == "ellas") or (pronoun == "ustedes"):
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ían"
        else:
            conjugatedVerb = verbRoot + "aban"
    if (pronoun == "nosotros") or (pronoun == "nosotras"):
        if (verbEnding == "ir") or (verbEnding =="er"):
            conjugatedVerb = verbRoot + "íamos"
        else:
            conjugatedVerb = verbRoot + "ábamos"

if tense == "future":
    if pronoun == "yo":
        conjugatedIr = "voy"
    elif pronoun == "tu":
        conjugatedIr = "vas"
    elif (pronoun == "usted") or (pronoun == "ella") or (pronoun == "el"):
        conjugatedIr = "va"
    elif (pronoun == "ellos") or (pronoun == "ellas") or (pronoun == "ustedes"):
        conjugatedIr = "van"
    elif (pronoun == "nosotros") or (pronoun == "nosotras"):
        conjugatedIr = "vamos"

    

print
if (tense == "present") or (tense == "past imperfect"):
    print "The verb conjugated is: " + pronoun.capitalize() + " " + conjugatedVerb + "."
else: 
    print "The verb conjugated is: " + pronoun.capitalize() + " " + conjugatedIr + " a " + verb +"."

    

    
