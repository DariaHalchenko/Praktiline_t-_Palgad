from ast import Lambda
from pickletools import read_stringnl_noescape
from sre_constants import ANY
from turtle import position


def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    param list i: Inimeste järjend
    param list p: Palgate järjend
    param int n: Inimeste arv
    rtype: list, list
    """
    if n>0:
        for j in range(n):
            nimi=(input("Nimi: ")).capitalize() 
            palk=int(input("Palk: ")) 
            i.append(nimi) 
            p.append(palk)
    return i,p  
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    param list i: Inimeste järjend
    param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j]) 
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimi=input("Keda kustutada ära(nimi): ") 
    for j in range(0,len(i)-1):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige suurim palk
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    palk=max(p) 
    n=p.count(palk) 
    positsiooni=0
    print("Maksimaalne palk:"+str(palk)) 
    for j in range(n):
        ind=p.index(palk,positsiooni)
        nimi=i[ind] 
        print(f"{nimi} on maksimaalne palk") 
        positsioni=ind+1 
        return i,p 

def kellel_on_vaiksem_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige väiksem palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    palk=min(p) 
    n=p.count(palk) 
    positsiooni=0
    print("Minimaalne palk:"+str(palk)) 
    for j in range(n):
        ind=p.index(palk,positsiooni)
        nimi=i[ind] 
        print(f"{nimi} on minimaalne palk") 
        positsioni=ind+1 
        return i,p 


def sorteeritud_palgad(i:list,p:list):
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p 

def sorteeritud_akahanevas_palgad(i:list,p:list):
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]<p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p 

def vordsed_palgad(i:list,p:list):
    """Funktsioon leiab inimesed kellel on võrdne palk
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    duplikaat=[x for x in p if p.count(x)>1]
    duplikaat=list(set(duplikaat)) 
    for palk in duplikaat:
        n=p.count(palk) 
        samde_palkade_arv=-1
        print(palk)
        for j in range(n):
            samde_palkade_arv=p.index(palk,samde_palkade_arv+1)
            nimi=i[samde_palkade_arv]
            print("Selliste inimeste palk on sama: "+str(nimi), (palk))
    return i,p

def palk_nime_jargi(i:list,p:list)->dict:
    """Funktsioon leiab palk nime järgi
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimi=input("Nimi: ").capitalize()
    palgad = []
    for j in range(len(i)):
        if i[j] == nimi:
            palgad.append(p[j])   
    print (nimi,"palgad on",palgad)
    return i,p


def palgaga_inimeste_nimekiri(i:list,p:list): 
    """Funktsioon leiab inimesed kes saavad rohkem/vähem kui määratud summa
        param list i: Inimeste järjend
        param list p: Palgate järjend
        rtype: list, list
    """
    palgad=int(input("1-rohkem või 2-vähem: "))
    summa=int(input("Palk: "))
    nimekiri=[] 
    if palgad==1:
        for j in range(len(i)):
            if summa<p[j]:
                nimekiri.append((i[j], p[j]))
        print("Nimekiri inimestest, kellel on palgad, kes saavad rohkem "+str(summa), "on" +str(nimekiri))
    elif palgad==2:
        for j in range(len(i)):
            if summa>p[j]:
                nimekiri.append((i[j], p[j]))
        print("Nende inimeste nimekiri, kes saavad vähem palka "+str(summa), "on" +str(nimekiri))
    return i,p


    
