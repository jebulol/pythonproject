x = input("Anna ikä")
ikä = int(x)

if ikä >= 18:
    if ikä < 20:
        x = input("Onko papereita? k/e")
        
        if x == "e":
            print("hae paperit")
        else:
            print("Tervetuloa sisään")
    if ikä >=20:            
        print("Tervetuloa sisään")
else:
    print("olet liian nuor1")
    
