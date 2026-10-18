diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
zmetek = 0
ok = 0
pozice = 0
for pozice, prumer in enumerate(diameters, start=1):
    if prumer > 25.05:

        print(f"{pozice} {prumer} VELKÝ" )
        zmetek += 1

    elif prumer < 24.95:
        print(f"{pozice} {prumer} MALÝ" )
        zmetek += 1
    else:

        print(f"{pozice} {prumer} OK" )
        ok += 1

print(f"Zmetků: {zmetek} / {zmetek + ok} = {(zmetek / (zmetek+ok))}")