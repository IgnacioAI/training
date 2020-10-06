import sqlite3

#Este comando estabelece uma conexão com o servidor
def acessoBanco(BancoDados, Comando):
    acess = sqlite3.connect(BancoDados)
    cursor = acess.cursor()
    #metodos de INSERT,DELETE,UPDATE
    cursor.execute(Comando)
    acess.commit()
    acess.close()
#Esta função é para trabalhar o SELECT "Seleção dos dados"
def acessSELECT(BancoDados,Comando):
    acess = sqlite3.connect(BancoDados)
    cursor = acess.cursor()
    cursor.execute(Comando)
    #este objeto recebe a RESPOSTA do comando SELECT (a tabela)
    table = cursor.fetchall()
    #como em geral é necessário imprimir a tabela, 
    #utilizamos um LOOP "FOR" para percorrer as linhas e executar a impressão
    for linha in table:
        print(linha)
#esta função vai trabalhar com todas as outras para manipular os dados no banco
#vou utlizar um banco de exemplo do qual eu já conheço a estrutura        
def setDados():
    #este comando vai inserir dados na tabela
    setInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado teste', 'sigla teste', 'cidade teste')"
    #armazene o caminho do BD por PATH num objeto
    pathBD = "C:\\Users\\Forasteiro\\Desktop\\Python_Estudos\\Python_Bootcamp\\projetoPython\\BancoDeDados.db"
    #adequando o SELECT
    setSelect = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"
    

#chamo a função que acessa o banco e recebe os parametros de
#banco de dados e os dados que vamos inserir
    acessoBanco(pathBD, setInsert)
#trabalhando com os dados pelo SELECT
    acessSELECT(pathBD,setSelect)
#executando o set de dados
setDados()

    