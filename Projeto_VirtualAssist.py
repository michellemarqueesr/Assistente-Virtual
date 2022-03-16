import pyttsx3 #Fala do Robo
import pyaudio #Auxilia na manipulação e execução do audio
from gtts import gTTS
from pygame import mixer
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import speech_recognition as sr #Reconhece sua fala


#Configurações Gerais - VOZ
tts = pyttsx3.init()
#Configurando volume e velocidade da assistente falará
tts.setProperty('rate',200)
tts.setProperty('volume',2.0)
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Lana':
        tts.setProperty('voice', voice.id)

#Recognizer para reconhecimento da voz
recon = sr.Recognizer()

#Variavel para utilizar quando houver execução da fala
requisicao = ''

#Opções para acessar através de lista
opcoes = ['Por favor, informe qual opção deseja acessar: ',
          '1. Efetuar busca no site',
          '2. Fechar o programa.']

#Execução do Assistente
tts.say('Olá, eu sou a Lana, sua assistente virtual. Vamos navegar pelo site do Governo!')
tts.runAndWait()
tts.say(opcoes)
tts.runAndWait()

while True:
    try:

        with sr.Microphone() as source:
            print('Ouvindo....')
            audio = recon.listen(source)
            requisicao = recon.recognize_google(audio, language='pt')

        #=====================================================================

        if 'Buscar no site' in requisicao:

            try:
                #Entrando no Navegador
                tts.say(f"Informe o que deseja pesquisar no site")
                tts.runAndWait()
                pesquisa = str(input('Informe o parâmetro de pesquisa: '))
                time.sleep(4)
                #executable_path do webdriver
                navegador = webdriver.Chrome(executable_path=r"C:\Users\alesi\chromedriver.exe")
                navegador.get('https://www.gov.br/pt-br')
                time.sleep(6)

                #Realizando busca
                #Escreve item a ser pesquisado
                navegador.find_element_by_xpath('//*[@id="searchtext-input"]').send_keys(pesquisa)
                time.sleep(6)

                #Clica
                navegador.find_element_by_xpath('//*[@id="searchtext-label"]/button').click()
                time.sleep(6)
                tts.say(f"Estes são os resultados da sua pesquisa")
                tts.runAndWait()
            except:
                tts.say(f"Houve um erro.")
                tts.runAndWait()
                raise Exception('Não foi possível executar. Tente novamente')

        # ======================================================================

        elif 'Fechar o programa' in requisicao:
            tts.say('Obrigada por acessar o Assistente Virtual do Governo. Encerrando programa. Até a próxima.')
            tts.runAndWait()
            break;
    except:
        tts.say('Não foi possível prosseguir. Encerrando...')
        tts.runAndWait()
        print('Não entendi a palavra', requisicao)
        break


