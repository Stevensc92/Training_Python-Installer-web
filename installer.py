# -*- coding: utf8 -*-
# Import python modules
import subprocess
import os
import sys
from modules import search

print("Ce script installera PHP ainsi qu'apache en fonction de la version php renseignée par la suite.")

startInstall = input("Voulez-vous démarrer l'installation ? [y/N] ")

# End script if answer isn't y

if startInstall.lower() != "y":
    print("Script d'installation interrompu")
    sys.exit()

inputTextPhpVersion = "Aucune version PHP détecté, la quelle souhaitez-vous installer ? "
phpVersion = input(inputTextPhpVersion)

while phpVersion == "":
    print("Vous devez saisir une version de PHP")
    phpVersion = input(inputTextPhpVersion)


phpName = "php"+phpVersion


#     print(cliSearch)
#     result = subprocess.check_output(["apt-cache", "search", phpName, "| grep", "-o", "^"+phpName+"-[[:alnum:]]\{1,\}"])
#     print(result)

search.searchPhpPacks(phpName)

search.existsPackage('software-properties-common')

