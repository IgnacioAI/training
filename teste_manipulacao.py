import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def criaZip():
    shutil.make_archive("ArquivoCompactado","zip", "C:\\Users\\Forasteiro\\OneDrive\\Documentos\\Arquivos de Exercicios")
    
#criaZip()

def criaZipModo2():
    with ZipFile("ArquivoCompactado.zip", "w") as novoZip:
        novoZip.write("NovoArquivo.bkp")
        novoZip.write("NovoArquivo.txt")
        novoZip.write("zipModo1.zip.zip")
        
#criaZipModo2()

def deleteArquivo():
    os.remove("ArquivoZipModo2.zip")

deleteArquivo()