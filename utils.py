import json
from database import Database
from database import Note


def extract_route(requisicao):
    '''
    lista_de_palavras = requisicao.split(' ')
    return lista_de_palavras[1][1:]
    '''
    #print("A REQUISICAO FOI: {}".format(requisicao))
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(path):
    list_extension = ['txt','js','html', 'css']
    text_or_bin = ""

    pathString = str(path)

    with open(pathString, 'rb') as s:
        text_or_bin = s.read()
    
    return text_or_bin

def load_data(archive):
    # path = "data/"+str(archive)
    # content = ""
    
    # with open (path, "r", encoding="utf-8") as json_archive:
    #     content = json_archive.read()
    
    # dict_json = json.loads(content)
    db = Database(archive)
    notes = db.get_all()
    
    return notes

def load_template(archive):
    path = "templates/"+str(archive)
    content = ""

    with open(path, "r") as html:
        content = html.read()
    
    return content

def build_response(body='', code=200, reason='OK', headers=''):
    

    string = "HTTP/1.1"  + " " + str(code) + " " + str(reason)
    if headers == '':
        string += '\n\n'+str(body)
    else:
        string += '\n'+headers+'\n\n' + str(body)

    return string.encode()

def save_data(newdict):
    db = Database('bancoNotes')
    
    newNote = Note(title = newdict['titulo'], content = newdict['detalhes']) 
    db.add(newNote)

def delete_data(id):
    db = Database('bancoNotes')
    db.delete(id)




    
    





