
vuosi = int(input("Anna vuosi "))
if((vuosi % 400 == 0) or  (vuosi % 100 != 0) and  (vuosi % 4 == 0)):
    print("vuosi on karkausvuosi");
else:
    print ("ei ole karkausvuosi")

