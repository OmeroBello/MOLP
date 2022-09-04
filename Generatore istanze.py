import random

scelta_int = 0

while scelta_int != 2:
    stringa = input("Inserisci il numero di job che vuoi schedulare: ")
    numero = int(stringa)

    i = 1
    tempi = []
    while i <= numero:
        tempi.append(random.randint(1, 100))
        i = i + 1
    tempi_stringa = "Tempi di processamento dei job: ["
    for x in tempi:
        tempi_stringa = tempi_stringa + str(x) + " "
    tempi_stringa = tempi_stringa + "]"
    print(tempi_stringa)

    i = 1
    pesi = []
    while i <= numero:
        pesi.append(random.randint(1, 20))
        i = i + 1
    pesi_stringa = "Pesi dei job: ["
    for x in pesi:
        pesi_stringa = pesi_stringa + str(x) + " "
    pesi_stringa = pesi_stringa + "]"
    print(pesi_stringa)

    scelta = input("Cosa vuoi fare? [1] per continuare, [2] per interrompere: ")
    scelta_int = int(scelta)
