#!/usr/bin/python3

print("hello word")

a = 1
if a == 0:
    print("toto")
else:
    print("a ne vaut pas 0")
print("fin")  



#Un entier 
entier = 1
#Un float 
fl = 1.5
#string 
string = "chaine1"
string = 'chaine1'
string = """il va dire "coucou" assf"""
"""
commentaire multiligne 
hzzbclzcuzvcue
"""

stringadd = "aa" + "bb"
print(stringadd)

if a == 0:
    string = ("coucou\n"
              "salut\n"
              "hello")

#nomenclature (style guide) PEP8

alphabet = "abcdefghijklmnopqrstuvwxyz"

if 'a' in alphabet:
    print(" j'ai trouvé a")

#tableau / list / array
alist = list()
alist = []
alist = ["a","b"]

#liste de int
alist = ["0","1","2","3","4"]
for x in alist:
    print(x)
print(alist)
alist = range(5)
print(alist)
for x in alist:
    print(x)

key = "fr"

trad = {"fr": "salut",
        "en": "hello"}
print(trad[key])

for key in trad:
    print(key)
    print(trad[key])

trad_fr = {"bjour" : "salut",
           "aie" : "j'ai mal"}
trad_en = {"bjour" : "hello"
           "aie" : "it hurts"}

#dictionnaire dans un dictionnaire 
trad = {"fr" : trad_fr,
        "en" : trad_en}

lang = "fr" 
print(trad[lang]['aie'])


alist = ["0","1","2","3","4"]
#list comprehension
list_comp = [x for x in alist]
list_comp = alist
print(list_comp)

list_comp = [x + "aa" for x in alist]
print(list_comp)

for x in alist:
    list_comp.append(x + "aa")
print(list_comp)

list_comp= []
for x in alist:
    list_comp.append(x + "aa")
print(list_comp)


#recuperer ma liste de langue a partir du dico
#rajouter key en liste 
trad = {"fr": "salut",
        "en": "hello"}
alist = [key for key in trad]
print("je gere les langues:",alist)

def add(a,b):
#function calc an addition
    return(a + b)

print(add(1,2))
print(add(10,20))

#fonction avec argument par défaut
def add3(a,b,c=0)
    return(a + b + c)

print(add3(1,2))
print(add3(10,20))
print(add3(10,20,30))
