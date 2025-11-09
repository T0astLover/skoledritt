import os 

#henter opperativsystemet til brukern og brukernavn
systemet = os.name
print("operativsystemet ditt er:", systemet)
#posix = linux/mac #NT = windows 

#måtte få hjelp av AI til denne delen men skal klare og forklare det :) 
import shutil 
storage = f"{shutil.disk_usage('C:\\').free / (1024**3):.2f} GB"
print("Ledig plass:", storage)

#brukernavn
username = os.getlogin()
print("brukernavnet ditt er:", username)

#ip adreesse
ipaddresse = os.popen("ipconfig").read()
print("ip adressen din er:", ipaddresse)

#apper
apper = os.popen("wmic product get name,version").read()
print(apper)

filsti = f"{username}.txt"

with open(filsti, "w") as fil:
    fil.write(f"Operativsystem: {systemet}\n")
    fil.write(f"Brukernavn: {username}\n")
    fil.write(f"lagring: {storage}\n")
    fil.write(f"IP adresse: {ipaddresse}\n")
    fil.write(f"Installerte apper: {apper}\n")
print(f"Informasjon lagret i filen: {filsti}")
#Ikke rydding men det fungerer :)
