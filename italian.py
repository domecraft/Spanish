#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created by Christopher Durr

'''

print "Welcome to the Italian verb conjugator!"
print
print "This program can conjugate any regular verb."
print
verb = raw_input("Enter the verb: ").lower()
verbRoot = verb[:len(verb) - 3]
verbEnding = verb[len(verb) - 3:]
tense = raw_input("Enter tense (E.g. present, past imperfect): ").lower()
print
print "Verb conjugation (%s)" % tense
tenseLength = len(tense) + 20
print "_"*tenseLength
if tense == "present":
    	if verbEnding == "are":
			print "Io: " + verbRoot + "o"
			print "Tu: " + verbRoot + "i"
			print "Lui/lui/lei: " + verbRoot + "a"
			print "noi: " + verbRoot + "iamo"
			print "voi: " + verbRoot + "ate"
			print "loro: " + verbRoot + "ano"
	elif verbEnding == "ere":
			print "Io: " + verbRoot + "o"
			print "Tu: " + verbRoot + "i"
			print "Lui/lui/lei: " + verbRoot + "e"
			print "noi: " + verbRoot + "iamo"
			print "voi: " + verbRoot + "ete"
			print "loro: " + verbRoot + "ono"
	elif verbEnding == "ire":
			print "Io: " + verbRoot + "o"
			print "Tu: " + verbRoot + "i"
			print "Lui/lui/lei: " + verbRoot + "e"
			print "noi: " + verbRoot + "iamo"
			print "voi: " + verbRoot + "ite"
			print "loro: " + verbRoot + "ono"
	else:
			print "Sorry, I couldn't conjugate that. Please try again."
elif (tense == "imperfect") or (tense == "past imperfect"):
		if verbEnding == "are":
			print "Io: " + verbRoot + "avo"
			print "Tu: " + verbRoot + "avi"
			print "Lui/lui/lei: " + verbRoot + "ava"
			print "noi: " + verbRoot + "avamo"
			print "voi: " + verbRoot + "avate"
			print "loro: " + verbRoot + "avano"
		elif verbEnding == "ere":
			print "Io: " + verbRoot + "avo"
			print "Tu: " + verbRoot + "evi"
			print "Lui/lui/lei: " + verbRoot + "eva"
			print "noi: " + verbRoot + "evamo"
			print "voi: " + verbRoot + "evate"
			print "loro: " + verbRoot + "evano"
		elif verbEnding == "ire":
			print "Io: " + verbRoot + "ivo"
			print "Tu: " + verbRoot + "ivi"
			print "Lui/lui/lei: " + verbRoot + "iva"
			print "noi: " + verbRoot + "ivamo"
			print "voi: " + verbRoot + "ivate"
			print "loro: " + verbRoot + "ivano"
		else: 
			print "Sorry, I couldn't conjugate that. Please try again."
elif (tense == "past"):
	if verbEnding == "are":
			print "Ho: " + verbRoot + "ato"
			print "Hai: " + verbRoot + "ato"
			print "Ha: " + verbRoot + "ato"
			print "abbiamo: " + verbRoot + "ato"
			print "avete: " + verbRoot + "ato"
			print "hanno: " + verbRoot + "ato"
	if verbEnding == "ere":
			print "Ho: " + verbRoot + "uto"
			print "Hai: " + verbRoot + "uto"
			print "Ha: " + verbRoot + "uto"
			print "abbiamo: " + verbRoot + "uto"
			print "avete: " + verbRoot + "uto"
			print "hanno: " + verbRoot + "uto"
	if verbEnding == "ire":
			print "Ho: " + verbRoot + "ito"
			print "Hai: " + verbRoot + "ito"
			print "Ha: " + verbRoot + "ito"
			print "abbiamo: " + verbRoot + "ito"
			print "avete: " + verbRoot + "ito"
			print "hanno: " + verbRoot + "ito"
elif (tense == "future") or (tense == "simple future") or (tense == "future simple"):
		if (verbEnding == "are") or (verbEnding == "ere"):
			print "Io: " + verbRoot + "erò"
			print "Tu: " + verbRoot + "erai"
			print "Lui/lui/lei: " + verbRoot + "erà"
			print "noi: " + verbRoot + "eremo"
			print "voi: " + verbRoot + "erete"
			print "loro: " + verbRoot + "eranno"
		elif verbEnding == "ire":
			print "Io: " + verbRoot + "irò"
			print "Tu: " + verbRoot + "irai"
			print "Lui/lui/lei: " + verbRoot + "irà"
			print "noi: " + verbRoot + "iremo"
			print "voi: " + verbRoot + "irete"
			print "loro: " + verbRoot + "iranno"
else:
		print "Sorry, I didn't understand the tense. Please try again."


pass
print "Thanks for using the program!"
