kilo = int (input("kilonuzu giriniz:"))
boy = int (input("boyunuzu giriniz: (cm)"))
boy = boy/100
indeks = kilo/(boy*boy)
print("Vücut kitle index'iniz {}".format(round(indeks)))
print ("İndeks: ", indeks)


if  indeks <=18.5 :
    print("zayıfsınız")
    print("{} kilo almanız gerekmektedir".format(round(25*(boy*boy) -kilo)))
elif indeks< 25 :
    print("kilonuz normaldir")
elif indeks < 30:
    print("kilonuz fazladır")
    print("{} kilo vermeniz gerekmektedir".format(kilo- round(25*(boy*boy) )))
elif indeks < 35:
    print("1. derece obezsinizdir")
    print("{} kilo vermeniz gerekmektedir".format(kilo- round(25*(boy*boy) )))
elif indeks < 40:
    print("2. derece obezsinizdir")
    print("{} kilo vermeniz gerekmektedir".format(kilo- round(25*(boy*boy) )))
elif indeks < 45:
    print("3. derece obezsinizdir")
    print("{} kilo vermeniz gerekmektedir".format(kilo- round(25*(boy*boy) )))
