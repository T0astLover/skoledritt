import os 
import platform

#henter opperativsystemet til brukern og brukernavn
try: 
    systemet = os.name
    osVersjon = platform.version()
    print("operativsystemet ditt er:", systemet + osVersjon)
except Exception as fkode:
    print("feil ved henting av OS", fkode)
#posix = linux/mac #NT = windows 

#måtte få hjelp av AI til denne delen men skal klare og forklare det :) 
import shutil 
try: 
    storage = f"{shutil.disk_usage('C:\\').free / (1024**3):.2f} GB"
    print("Ledig plass:", storage)
except Exception as fkode:
    print("feil ved henting av lagring", fkode)

#brukernavn
try:
    username = os.getlogin()
    print("brukernavnet ditt er:", username)
except Exception as fkode:
    print("feil ved henting av brukernavn", fkode)

#ip adreesse
try: 
    ipaddresse = os.popen("ipconfig").read()
    print("ip adressen din er:", ipaddresse)
except Exception as fkode:
    print("feil ved henting av ip adresse", fkode)

#apper
try:
    apper = os.popen("wmic product get name,version").read()
    print(apper)
except Exception as fkode:	
    print("feil ved henting av apper", fkode)

#lager filen med brukernavet
filsti = f"{username}.txt"

#skriver in infoen til filen
try:
    with open(filsti, "w") as fil:
        fil.write(f"Operativsystem: {systemet} {osVersjon}\n")
        fil.write(f"Brukernavn: {username}\n")
        fil.write(f"lagring: {storage}\n")
        fil.write(f"IP adresse: {ipaddresse}\n")
        fil.write(f"Installerte apper: {apper}\n")
    print(f"Informasjon lagret i filen: {filsti}")
except Exception as fkode:
    print("feil ved lagring av fil", fkode)
