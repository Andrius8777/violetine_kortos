import random

def sukurti_kortu_kalade():
    simboliai = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    zenklai = ['♠', '♡', '♢', '♣']
    kortos_kalade = [{'simbolis': simbolis, 'zenklas': zenklas} for simbolis in simboliai for zenklas in zenklai]
    random.shuffle(kortos_kalade)
    return kortos_kalade

def dalinti_kortas(kalade):
    zaideju_kortos = [[], []]
    for i in range(len(kalade)):
        zaideju_kortos[i % 2].append(kalade[i])
    return zaideju_kortos

def karas(zaideju_kortos):
    stalo_kortos = []
    while zaideju_kortos[0] and zaideju_kortos[1]:
        korta1 = zaideju_kortos[0].pop(0)
        korta2 = zaideju_kortos[1].pop(0)
        
        stalo_kortos.extend([korta1, korta2])
        print(f"Žaidėjas 1: {korta1['simbolis']} {korta1['zenklas']} | Žaidėjas 2: {korta2['simbolis']} {korta2['zenklas']}")
        
        if korta_verte(korta1) > korta_verte(korta2):
            zaideju_kortos[0].extend(stalo_kortos)
            stalo_kortos = []
            print("Žaidėjas 1 laimi!")
        elif korta_verte(korta1) < korta_verte(korta2):
            zaideju_kortos[1].extend(stalo_kortos)
            stalo_kortos = []
            print("Žaidėjas 2 laimi!")
        else:
            print("Lygiosios! Karas!")

def korta_verte(korta):
    simbolio_reiksmes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return simbolio_reiksmes[korta['simbolis']]

if __name__ == "__main__":
    kalade = sukurti_kortu_kalade()
    zaideju_kortos = dalinti_kortas(kalade)
    karas(zaideju_kortos)