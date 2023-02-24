from bs4 import BeautifulSoup
import requests
import pandas as pd

i = 1
podaci = {
    "Marka": [],
    "Model": [],
    "Predjena kilometraza": [],
    "Godiste": [],
    "Gorivo": [],
    "Cijena": [],
    "Grad": [],
    "Vrijeme objave": []
}

while i != 278:
    url = f"https://www.autodiler.me/automobili/all/{i}"
    lok = requests.get(url)
    lok.raise_for_status()
    soup = BeautifulSoup(lok.text, 'html.parser')
    auta = soup.find('div', class_="oglasi-content-text")

    for kola in auta:
        
        lista = kola.find('div', class_="oglasi-item-tekst-tekst").text
        niz = lista.split()
        
        if len(niz) < 6:
            print("//")
        elif len(niz) == 6:
            km = niz[1]
            km = km.replace("km", "")
            god = niz[3]
            gorivo = niz[5]
        elif len(niz) > 6:
            if niz[6] == "dizel" or niz[6] == "benzin":
                km = niz[1]
                km = km.replace("km", "")
                god = niz[3]
                gorivo = niz[5]+"-"+niz[6]        
            else:
                km1 = niz[2]
                km = km1.replace("km", "")
                km = niz[1]+km
                god = niz[4]
                gorivo = niz[6]        
        else:
            print("//")
    
    
        lokacija = kola.find('div', class_="oglasi-mesto").p.text
        naziv = kola.find('a', class_="oglasi-item-heading").text
        niz2 = naziv.split("-")
        cijena = kola.find('div', class_="cena").p.text
        vrijeme = kola.find('div', class_="oglasi-vreme").text
        
        if len(niz2) > 1 and len(niz) > 2:
            if vrijeme.startswith("prije"):
                if (vrijeme.endswith("min") or vrijeme.endswith("h")):
                    vrijeme = "07.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 1 dan")):
                    vrijeme = "06.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 2 dana")):
                    vrijeme = "05.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 3 dana")):
                    vrijeme = "04.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 4 dana")):
                    vrijeme = "03.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 5 dana")):
                    vrijeme = "02.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 6 dana")):
                    vrijeme = "01.02.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                elif (vrijeme.startswith("prije 7 dana")):
                    vrijeme = "31.01.2023"
                    podaci["Vrijeme objave"].append(vrijeme)
                else:
                    podaci["Vrijeme objave"].append(vrijeme)


                podaci["Marka"].append(niz2[0])
                podaci["Model"].append(niz2[1])
                podaci["Cijena"].append(cijena)
                podaci["Predjena kilometraza"].append(km)
                podaci["Godiste"].append(god)
                podaci["Gorivo"].append(gorivo)
                podaci["Grad"].append(lokacija)
          
            else:
                if vrijeme.endswith("23"):
                    podaci["Marka"].append(niz2[0])
                    podaci["Model"].append(niz2[1])
                    podaci["Cijena"].append(cijena)
                    podaci["Vrijeme objave"].append(vrijeme)
                    podaci["Predjena kilometraza"].append(km)
                    podaci["Godiste"].append(god)
                    podaci["Gorivo"].append(gorivo)
                    podaci["Grad"].append(lokacija)              
                elif vrijeme.endswith("22"):
                    podaci["Marka"].append(niz2[0])
                    podaci["Model"].append(niz2[1])
                    podaci["Cijena"].append(cijena)
                    podaci["Vrijeme objave"].append(vrijeme)
                    podaci["Predjena kilometraza"].append(km)
                    podaci["Godiste"].append(god)
                    podaci["Gorivo"].append(gorivo)
                    podaci["Grad"].append(lokacija)          
                else:
                    print("//")

        else:
            print("//")
    print(i,".", "strana")
    i = i+1
    
N = pd.DataFrame(podaci)
N.to_excel("autafinal3.xlsx")
