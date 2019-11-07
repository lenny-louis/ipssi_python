import os
import sys

#mes arguments
print(sys.argv)

# / unix ...
# \Windows
#mal l'utilise = ...path = "/home/kit"

print(os.path.join("home", "kit"))


#trier résultat 
dir(os)
for x in dir(os):
    if "dir" in x:
        print(x)
