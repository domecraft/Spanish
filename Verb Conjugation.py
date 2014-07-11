print "Please note, this program will only work for regular verbs"

inputtCorrect = False
while inputtCorrect == False:
    tense = raw_input("Enter the tense of the verb (past imperfect, past, present or future): ")
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
    pronoun = pronoun.lower()
    try:
        int(pronoun)
    except:
        inputpCorrect = True
    print 
inputwCorrect = False
while inputwCorrect == False:
    print
    verb = raw_input("Enter the infinitive of the verb: ")
    verb = verb.lower()
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
    elif (pronoun == "vosotros") or (pronoun == "vosotras"):
        if (verbEnding == "er") or (verbEnding == "ir"):
            conjugatedVerb = verbRoot + "éis"
        else:
            conjugatedVerb = verbRoot + "áis"
            
if tense == "past imperfect":
    if pronoun == "yo":
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ía"
        else:
            conjugatedVerb = verbRoot + "aba"
    elif pronoun == "tu":
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ías"
        else:
            conjugatedVerb = verbRoot + "abas"
    elif (pronoun == "usted") or (pronoun == "el") or (pronoun == "ella"):
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ía"
        else:
            conjugatedVerb = verbRoot + "aba"
    elif (pronoun == "ellos") or (pronoun == "ellas") or (pronoun == "ustedes"):
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "ían"
        else:
            conjugatedVerb = verbRoot + "aban"
    elif (pronoun == "nosotros") or (pronoun == "nosotras"):
        if (verbEnding == "ir") or (verbEnding =="er"):
            conjugatedVerb = verbRoot + "íamos"
        else:
            conjugatedVerb = verbRoot + "ábamos"
    elif (pronoun == "vosotros") or (pronoun == "vosotras"):
        if (verbEnding == "ir") or (verbEnding == "er"):
            conjugatedVerb = verbRoot + "íais"
        else:
            conjugatedVerb = verbRoot + "abais"
            
if tense == "past":
    if pronoun == "yo":
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "é"
        else:
            conjugatedVerb = verbRoot + "í"
    elif pronoun == "tu":
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "aste"
        else:
            conjuguatedVerb = verbRoot = "iste"
    elif (pronoun == "usted") or (pronoun == "ella") or (pronoun == "el"):
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "ó"
        else:
            conjuguatedVerb = verbRoot + "ió"
    elif (pronoun == "ustedes") or (pronoun == "ellos") or (pronoun == "ellas"):
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "aron"
        else:
            conjugatedVerb = verbRoot + "ieron"
    elif (pronoun == "nosotros") or (pronoun == "nosotras"):
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "amos"
        else:
            conjugatedVerb = verbRoot + "imos"
    elif (pronoun == "vosotros") or (pronoun == "vosotras"):
        if verbEnding == "ar":
            conjugatedVerb = verbRoot + "asteis"
        else:
            conjugatedVerb = verbRoot + "isteis"
        
            

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
    elif (pronoun == "vosotros") or (pronoun == "vosotras"):
        conjugatedIr = "vais"
    

    

print ""
if (tense == "present") or (tense == "past imperfect") or (tense == "past"):
    print "The verb conjugated is: " + pronoun.capitalize() + " " + conjugatedVerb + "."
else: 
    print "The verb conjugated is: " + pronoun.capitalize() + " " + conjugatedIr + " a " + verb +"."

    

    
