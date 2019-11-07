#a = input( " entrez un nombre : ")
#if 'a%2 = 0':
 #   print("pair")
#else:    
#    print("impair")

#ou ça c'est bon
 
#a = 6

#if a%2 == 0:
 #   print("pair")
#else:
   # print("impair")

from datetime import datetime

d = datetime.now()
print(d)
print(d.day)
print(d.minute)
print(d.month)

print("type de day",type(d.day))
if d.day % 2:
    print("le jour est impair")
else:
     print("le jour est pair")

#pas le droit de concatener un int sur une string 
#print("le numero du jour est" + d.day")

#print("le numero du jour est ",d.day,"fin")
#print("le numero du jour est " str(d.day) + "fin")
print("le numero du jour est {} fin".format(d.day)) 
