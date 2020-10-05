import urllib.request

def acessoSite():
    objurl = urllib.request.urlopen("http://www.google.com.br")
    if objurl.getcode() == 200:
        dados = objurl.read()
        print(dados)
        
#acessoSite()

# trabalhando com arquivos JSON

import urllib.request
import json

def dadosJSON():
    eDados = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    webURL = urllib.request.urlopen(eDados)
    if (webURL.getcode() == 200):
        dados = webURL.read()
        objJSON = json.loads(dados)
        
        contagem = objJSON["metadata"]["count"] 
        print("Contage: " + str(contagem))
        
        for local in objJSON["features"]:
            if local["properties"]["place"] == "27 km SSE of Mina, Nevada":
                print("*** REGISTRO LOCALIZADO ***")
            else:
                print(local["properties"]["place"])
            
dadosJSON()
       
    