#!/usr/bin/env python

# Pepa píše program

# Pepa je chytrý, proto vyvíjí v dev

# Na tento velký projekt přibyl Franta, který dostal za úkol implementovat novou featuru (Dělá to, že nedělá nic)
# (Tyto dva řádky napsal Franta)

# Franta dostal specifikace od Jany a Amálky a mohl tak začít programovat na své části projektu
# Jeho úkolem bylo naprogramovat
#  - funkci, která volá Amálčinu funkci, pak dělá nějaké výpočty a nakonec nevrátí nic
#  - funkci, která volá v cyklu Amálčinu funkci

from importantFunction import importantFunction

def functionThatDoesNothing1():
	importantFunction()
	a = 1
	b = 2
	c = a + b
	return

def functionThatDoesNothing1():
	for i in range(10):
		importantFunction()
