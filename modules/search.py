# -*- coding: utf8 -*-
import os
import subprocess
import re

def searchPhpPacks(phpName):
    cliSearch = 'apt-cache search "'+phpName+'" | grep -o "^'+phpName+'-[[:alnum:]]\{1,\}"'
    os.system(cliSearch)

def existsPackage(packageName):
    cliSearch = 'dpkg -l | grep "'+packageName+'"'
    resultCli = returnResultFromCli(cliSearch)
    ifInstalled = resultCli.split()[0]
    if ifInstalled != 'ii':
        toInstall = input('Le paquet '+packageName+' est manquant, pour poursuivre l\'installation souhaitez-vous l\'installer ? [Y/n]')
        if toInstall.lower() == 'y':
            installPackage(packageName)

    print('ExistPackage function return : \n')
    print(type(resultCli))


def returnResultFromCli(command):
    ps = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('utf-8')
    return output

def installPackage(packageName):
    cmd = 'apt-get install -y '+packageName
    return os.system(cmd)