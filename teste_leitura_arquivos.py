def criar_novo():
    arquivo = open ("NovoArquivo.txt","w+")
    arquivo.write("Linha gerada por função 'Escreve arquivo' \r\n")
    
    arquivo.close()
    
#criar_novo()

def alterar_novo():
    arquivo = open ("NovoArquivo.txt","a+")
    arquivo.write("Linha gerada por funcao 'Altera arquivo' \r\n")
    
    arquivo.close()
    
#alterar_novo()

def leitura_arquivo():
    arquivo = open("NovoArquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudo = arquivo.read()
        print(conteudo)
        
    arquivo.close()
    
#leitura_arquivo()

#from docx import Document
#document = Document()
#desenvolver estrutura para leitura de arquivos docx

def leitura_arquivoGrande():
    document = open("NovoArquivo.txt", "r")
    if (document.mode == "r"):
        conteudoTotal = document.readlines()
        
        for conteudo in conteudoTotal:
            print(conteudo)
        
    document.close()
    
#leitura_arquivoGrande()

from os import path
import time

def dadosArquivos():
    arquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir("NovoArquivo.txt")
    patArquivo = path.realpath("NovoArquivo.txt")
    patRelativo = path.relpath("NovoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))
    
    print(arquivoExiste)
    print(ehDiretorio)
    print(patArquivo)
    print(patRelativo)
    print(dataCriacao)
    print(dataModificacao)
    
#dadosArquivos()
import os 
from os import path
import shutil

def copiarArquivo():
    if path.exists("documentação_pythondocx.txt"):
        pathAtual = path.realpath("documentação_pythondocx.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)
        
        shutil.copystat(pathAtual, novoPath)
        
#copiarArquivo()

def renomearArquivo():
    if path.exists("documentação_pythondocx.txt.bkp"):
     os.rename("documentação_pythondocx.txt.bkp","DocPythondocx.txt")
    
renomearArquivo()
               


