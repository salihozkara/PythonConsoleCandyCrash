import random
import string
def getRandom():
    return random.choice(string.ascii_letters[:5]).upper()


def satirOlustur(satirUzunlugu):
    satir=[]
    for i in range(satirUzunlugu):
        satir.append(getRandom())
    return satir


def matrisOlustur(matrisBoyut):
    matris=[]
    for i in range(matrisBoyut):
        matris.append(satirOlustur(matrisBoyut))
    return matris


def matrisYazdir(matris):
    print("-----------------------------------------")
    s=0
    def sutunNoYaz():
        print("  ",end="")
        for i in range(len(matris)):print("  "+str(i),end="  ")
        print()
    sutunNoYaz()
    for i in matris:
        print(s,i,s)
        s+=1
    sutunNoYaz()
    print("-----------------------------------------")

def kaydir(matris,i,j):
    for k in range(i,-1,-1):
        if k>0:
            matris[k][j]=matris[k-1][j]
        else:
            matris[k][j]=getRandom()
    matrisKontrol(matris)


def matrisKontrol(matris):
    for i in range(len(matris)):
        for j in range(len(matris)-2):
            if matris[i][j]==matris[i][j+1] and matris[i][j]==matris[i][j+2]:
                a=3
                while(j+a+1<len(matris) and matris[i][j]==matris[i][j+a]):
                    a+=1
                for k in range(a):
                    kaydir(matris,i,j+k)
            if matris[j][i]==matris[j+1][i] and matris[j][i]==matris[j+2][i]:
                a=3
                while(j+a+1<len(matris) and matris[j][i]==matris[j+a][i]):
                    a+=1
                for k in range(a):
                    kaydir(matris,j+k,i)
    return matris


def kaydir2(matris,i,j,yon,yon2):
    matris[i][j],matris[i+yon][j+yon2]=matris[i+yon][j+yon2],matris[i][j]

def oyun():
     matris=matrisOlustur(10)
     while(True):
        matrisKontrol(matris)
        matrisYazdir(matris)
        i=int(input("i:"))
        j=int(input("j:"))
        yon=input("yon:")
        yon1=0
        yon2=0
        if yon=='r':
            yon2+=1
        elif yon=='l':
            yon2-=1
        elif yon=='u':
            yon1-=1
        elif yon=='d':
            yon1+=1
        kaydir2(matris,i,j,yon1,yon2)
        
         
oyun()