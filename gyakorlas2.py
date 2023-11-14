import random
import math
## véletlen számok generálása




"Generálj 5 véletlen lottószámot [1,90]"
def feladat1():
    i: int = 0
    while i < 5:
        szam: int = math.floor(random.random() * 89+1)
        print(szam, end=" ")
        i += 1




    #2.feladat
    #generálj egy random számot , döntsde el róla hogy páros vagy páratan
def feladat2():
    i:int=0
    while i<1:
        szam:int=math.floor(random.random()*89+10)
    if szam % 2 ==0:
        print("páros")
    else:
        print("Páratlan")
        i+=1




    #3.feladat
    #generálj 15 db egész számot [0,1] között, hány 1 generált?
def feladat3():
        i: int = 0
        while i < 15:
            szam = random.random() * 1 + 0
            print(szam, end=" ")
            i += 1




    #4.generálj véletelen számot 1 és 10 között
    #szorozd meg 3 mal
    #vonj ki belőle 15-öt
    #oszd el 6-tal
    #szorozd meg 2-vel
    #vond ki belőle az eredeti számot
    #A program írja ki, hogy az eredmény egynelő-e 5-tel?
def feladat4():
    veletlen_szam = random.random()
    szam = int(veletlen_szam * 10) + 1
    eredmeny = (((szam * 3) - 15) / 6) * 2 - szam
    print(f"Az eredmény ({eredmeny}) egyenlő-e 5-tel? {eredmeny == 5}")



#5. feladat
# #Irj metódust, mely a paraméterben kapott szövegnek kiirja a hosszát
# az 5. karakterét nagybetűvel
def feladat5(text):
    print(f"A szöveg hossza: {len(text)}")
    if len(text) >= 5:
        print(f"Az 5. karakter nagybetűvel: {text[4].upper()}")
    else:
        print("A szöveg rövidebb, mint 5 karakter.")
