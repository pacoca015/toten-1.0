# Codigo para o projeto dos totens
# Feito por Gustavo Franden Pereira e Arthur Aurelio de Almeida
# Contato: gustavopereirabreda@gmail.com
# Bibliotecca usada para a confeccao do ccodigo
# codigo para o projeto dos totens
# Laboratorio de agentes inteligentes LAI
# 19 de agosto de 2022
# bibliotecas usada para a confeccao do ccodigo
import pyautogui
import RPi.GPIO as GPIO
import time


# contador que sera usado para o lado direito
contador_baixo = 0
contador_click = 0


GPIO.setmode (GPIO.BCM)


#Configuração dos pinos GPIO do raspberry
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#Operação de converção dos pinos do raspberry
def ope(operacao):
        if (operacao == 'c' ):
            clicks()
        if (operacao == 's'):
            separador()
        if (operacao == 'e'):
            separador_esquerda()
        if (operacao == 'v'):
            volta()

# Funcao que levara para volta
# Essa função serve para voltar as paginas do site ou entâo para voltar para a seção da esquerda
def volta():
    global contador_click
    global contador_baixo

    if contador_click == 1:
        contador_baixo = 1
        x = 80
        y = 250
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)
        contador_click = 0

    if contador_click == 2:
        x = 1850
        y = 1000
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)
        pyautogui.click()
        contador_baixo = 1
        baixo_direito()
        contador_click = 1


# Funcao que levara para cima no lado direito do site
def cima_direito():
    global contador_baixo
    global contador_cima

    contador_baixo = contador_baixo - 1

    if contador_baixo == 1:
        x = 600
        y = 350
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)

    if contador_baixo == 2:
        x = 600
        y = 650
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)

    if contador_baixo == 3:
        x = 600
        y = 900
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)

    if contador_baixo == 0:
        x = 600
        y = 950
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(-10)

        contador_baixo = 4

    if contador_baixo == -1:
        x = 600
        y = 900
        pyautogui.moveTo(x, y, duration=0.01)
        contador_baixo = 3
        pyautogui.scroll(10)


# Funcao que levara para cima no lado esquerdo do site
def cima_esquerdo():
    global contador_baixo
    global contador_cima

    contador_baixo = contador_baixo - 1
    

    if contador_baixo == 1:
        x = 80
        y = 250
        pyautogui.moveTo(x, y, duration=0.01)
      

    if contador_baixo == 2:
        x = 80
        y = 300
        pyautogui.moveTo(x, y, duration=0.01)
        

    if contador_baixo == 3:
        x = 80
        y = 350
        pyautogui.moveTo(x, y, duration=0.01)
       

    if contador_baixo == 0:
        x = 80
        y = 400
        pyautogui.moveTo(x, y, duration=0.01)
        contador_baixo = 4

    if contador_baixo == -1:
        x = 80
        y = 450
        pyautogui.moveTo(x, y, duration=0.01)
        contador_baixo = 3


# Funcao que levara para baixo do lado esquerdo
def baixo_esquerda():
    global contador_baixo
    global contador_cima

    contador_baixo = contador_baixo + 1

    if contador_baixo == 1:
        x = 80
        y = 250
        pyautogui.moveTo(x, y, duration=0.01)
       

    if contador_baixo == 2:
        x = 80
        y = 300
        pyautogui.moveTo(x, y, duration=0.01)
        

    if contador_baixo == 3:
        x = 80
        y = 350
        pyautogui.moveTo(x, y, duration=0.01)
       

    if contador_baixo == 4:
        x = 80
        y = 400
        pyautogui.moveTo(x, y, duration=0.01)

        contador_baixo = 0


# Função separadora serve para para o programa entender se a função cima sera realizada na direira ou na esquerda
def separador_esquerda():
    global contador_click

    if contador_click == 0:
        cima_esquerdo()
    else:
        cima_direito()


# Função separadora serve para para o programa entender se a função baixo sera realizada na direira ou na esquerda
def separador():
    global contador_click

    if contador_click == 0:
        baixo_esquerda()

    else:
        baixo_direito()

# Funcao que levara para baixo do lado direito
def baixo_direito():


    global contador_baixo
    global contador_cima

    contador_baixo = contador_baixo + 1

    if contador_baixo == 1:
        x = 600
        y = 350
        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(10)

    if contador_baixo == 2:
        x = 600
        y = 650

        pyautogui.moveTo(x, y, duration=0.01)

    if contador_baixo == 3:
        x = 600
        y = 900

        pyautogui.moveTo(x, y, duration=0.01)

    if contador_baixo == 4:
        x = 600
        y = 950

        pyautogui.moveTo(x, y, duration=0.01)
        pyautogui.scroll(-10)
        contador_baixo = 0



# Funcao que contara os cliques do usuario para que entao a função separadora funcione
def clicks():
    global contador_click
    global contador_baixo
    contador_click = contador_click + 1

    contador_baixo = 1
    pyautogui.click()
    x = 600
    y = 350
    pyautogui.moveTo(x, y, duration=0.01)

    if contador_click > 2:
        contador_click = 2


# Loop que fica responsavel para deixar o programa rodando pelo tempo que o raspberry pi estiver ligado
while True:
    
    operacao = 'x'
    
    input_statee = GPIO.input(26)
    if input_statee == False:
        operacao = 'v'
        ope(operacao)
        time.sleep(0.5)
        operacao = 'x'

    input_states = GPIO.input(19)
    if input_states == False:
        operacao = 'e'
        ope(operacao)
        time.sleep(0.5)
        operacao = 'x'

    input_statew = GPIO.input(13)
    if input_statew == False:
        operacao = 'c'
        ope(operacao)
        time.sleep(0.5)
        operacao = 'x'
        
    input_stated = GPIO.input(6)
    if input_stated == False:
        operacao = 's'
        ope(operacao)
        time.sleep(0.5)
        operacao = 'x'
        
