from html.parser import HTMLParser

class  meuParser(HTMLParser):  # classe que herda os metodos da classe HTMLParser para exibir mensagens personalizadas  
    def handle_starttag(self, tag, attrs):       #substituindo metodos e verifica se foi encontrado uma tag de abertura
        print("Tag de abertura encontrada")
        if attrs.__len__() > 0: # se ele contiver valores eles serão impressos
            for a in attrs: # loop de impressão dos valores das tags
                print(" Valores encontrados: " , a[0], " = ", a[1])

    def handle_endtag(self, tag):  #metodo que vai manipular a tag de fechamento
        print(" TAG de fechamento encontrada")
        
    #metodo que verifica se um comentário foi encontrado
    def handle_comment(self, data):
        print("Comentário localizado")
        
    # metodo que verifica se valores são encontrados
    def handle_data(self, data):
        print(" Valores localizados")
        if data.isspace():
            print(" Valor encontrado é um espaço")
        else:
            print(" Valor localizado é : ", data)
            
    # função que vai instaciar um objeto
def meuObjeto():
    meuparser1 = meuParser()
#metodo feed que vai ler um arquivo
    arquivo = open("Login_v2.html", "r" )
    dados = arquivo.read()
    meuparser1.feed(dados)
    
meuObjeto()
    
