## Based in code found at
## https://betterprogramming.pub/how-to-create-your-own-text-replacement-tool-with-python-60a9e4ee8461
##
## Pyautogui replaced by Controller
## includes #end command
##
## Fiz essa versão com algumas melhorias do código encontrado no link acima
## Tentei usar o GlobalHotkeys do Pynput mas ele tem um bug na versão atual 
## Usar o código com '#' para iniciar a macro foi a melbor solução no momento


# Imports
## Pynput para ler os eventos do teclado
from pynput.keyboard import Key, Listener, Controller

replacements = {"nome": "Primeiro Nome Sobrenome",
                "mail": "email@servidor.com.br"}

macro_starter = '#'
macro_ender = Key.space
typed_keys = []
listening = True

# Iniciar o Controller é necessário para poder mandar os keypress
keyboard = Controller()

def on_press(key):
    global typed_keys
    global listening

    key_str = str(key).replace('\'', '')
    # verifica se a tecla pressionada é a de inicio de macro, no caso #
    if key_str == macro_starter:
        typed_keys = []
        listening = True

    # começa a armazer o texo a procura de um nome de macro
    if listening:
        if key_str.isalpha():
            typed_keys.append(key_str)
        
        # se encerrou o nome da macro, no caso usamos espaço, aí busca no dicionario se existe texto a ser substituído
        if key == macro_ender:
            candidate_keyword = ""
            candidate_keyword = candidate_keyword.join(typed_keys)

            if candidate_keyword != "":
                if candidate_keyword in replacements.keys():
                    # esse loop vai apagar o nome da macro para depois substituir o texto
                    for _ in range(len(candidate_keyword)+2):
                        keyboard.tap(Key.backspace)
                    keyboard.type(replacements[candidate_keyword])

                elif candidate_keyword == "end":
                    listener.stop()
                    print("Stopped")

            listening = False

# aqui inicia o thread que vai monitorar o teclado, não é preciso estar com foco no programa
# a macro vai substituir onde for digitada
with Listener(on_press=on_press) as listener:
   listener.join()
