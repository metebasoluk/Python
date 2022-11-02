while True:
    sayi=input("\nBir çift sayı gir: ")
    if sayi=="q":
        break
    elif (int(sayi)%2!=0):
        print("\nTek sayı girdin.")
        continue
    asalbolenler=[]
    sayilar=[]
    for k in range(2,int(sayi)):
        sayilar.append(k)
    for i in sayilar:
        sayac=0
        for z in range(2,i):
            if i%z==0:
                sayac=1
        if sayac==0:
            asalbolenler.append(i)
    toplamlar=[]
    a=len(asalbolenler)
    for i in asalbolenler:
        x=0
        while x<a:
            if i+asalbolenler[x]==int(sayi):
                toplamlar.append(f"{i}+{asalbolenler[x]}")
                break
            x+=1
    if len(toplamlar)%2==0:
        a=int(len(toplamlar)/2)
        del toplamlar[0:a]
    else:
        a=int(len(toplamlar)/2)
        del toplamlar[0:a]
    for i in toplamlar:
        print(f"\n{i}")