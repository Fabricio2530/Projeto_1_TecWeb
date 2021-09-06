from utils import load_data, load_template, build_response, save_data
import urllib
from os import error, replace

def index(request):
    note_template = load_template('components/note.html')
    params = {}
    response = build_response()
    #print(request)

    print('\n' + request)
    if request.startswith('POST'):
     
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")

        save_data(params)
        
        print("Os parâmetros são: {}".format(params))

        response = build_response(code=303, reason='See Other', headers='Location: /')
        
        
    
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in load_data('bancoNotes')
    ]
    notes = '\n'.join(notes_li)

    return response+load_template('index.html').format(notes=notes).encode()