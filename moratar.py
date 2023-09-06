milleja = int(input("Kuinka monta milliä täysin zoomatulla kartalla on yksi ruutu (100m):"))

while True:
    print("")
    print("MORTAAAAR KOMBAAT")
    print("")
    try:
        arvo = int(input("Paljonko mittaetäisyys milleinä?"))
    except ValueError:
        print("Vitun homo")
    zoom = int(input("Onko zoomi 1 (lähin), 2(yksi naksu takasinpäin), 3(jne.):"))
    if zoom == 1:
        zoomi = 1
    else:
        zoomi = int(2**(zoom-1))
    print("")   
    print("PUBG metreinä arvo on:")
    tulostus = (arvo/milleja)*100*zoomi
    print(int(tulostus))
    print("")
