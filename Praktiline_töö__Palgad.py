from MoodulPalgadele import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"] 
while True:
    print("0-Naita andmed veerudes\n1-andemete lisamine\n2-andmete kustutamine\n3-kõige suurim palk\n4-kõige väiksem palk\n5-sorteeritud palgad\n") 
    valik=int(input()) 
    if valik==1:
        inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
        andmed_veerudes(inimesed,palgad)
    elif valik==0:
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed, palgad) 
    elif valik==3:
        kellel_on_suurim_palk(inimesed, palgad) 
    elif valik==4:
        kellel_on_vaiksem_palk(inimesed, palgad)
    elif valik==5:
        sorteeritud_palgad(inimesed, palgad) 
        print(inimesed, palgad) 
    elif valik==6:
        sorteeritud_akahanevas_palgad(inimesed, palgad)
        print(inimesed, palgad)
    elif valik==7:
        vordsed_palgad(inimesed, palgad)
    elif valik ==8:
        palk_nime_jargi(inimesed, palgad) 
    elif valik ==9:
        palgaga_inimeste_nimekiri(inimesed, palgad)
