# TalentoCloud
andar = 20
while andar > -1:
    if andar == 13:
       andar -= 1
       continue
    else:
        print(f"{andar}° andar")
        andar -= 1
    time.sleep(1)
print("Este prédio não possui o 13° andar") 
