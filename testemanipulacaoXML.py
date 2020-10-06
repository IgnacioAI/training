import xml.dom.minidom

def dadosXML():
    doc = xml.dom.minidom.parse("C:\\Users\\Forasteiro\\Desktop\\Python_Estudos\\Python_Bootcamp\\projetoPython\\exemploXML.xml")
    print("Esta é a primeira tag: ",str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName("firstname")
    print("O primeiro nome é: ",primeiroNome[0].firstChild.nodeValue)
    
    
    for skill in doc.getElementsByTagName("skill"):
        print(" Skills encontradas: ",skill.getAttribute("name"))
        
dadosXML()