import tweepy
from datetime import datetime, date
import os
from os import environ
import time

while True:#rotina para o codigo atualizar a cada 15 segundos
    #tokens de acesso à conta do twitter
    API_KEY = environ['API_KEY']
    API_SECRET_KEY = environ['API_SECRET_KEY']
    ACCESS_TOKEN = environ['ACCESS_TOKEN']
    ACCESS_SECRET_TOKEN = environ['ACCESS_SECRET_TOKEN']

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    api = tweepy.API(auth)

    enem = date(2021, 11, 21) #Dia da primeira fase
    agora = date.today() #Dia de hoje

    enemDiasHoras = str(enem - agora) # Diferença entre os dias colocados anteriormente
    enemDias = enemDiasHoras[0:3] #para tirar o horario e me dar somente os dias

    primeiraFase = date(2021, 11, 7) #Dia da primeira fase

    primeiraFaseDiasHoras = str(primeiraFase - agora) # Diferença entre os dias colocados anteriormente
    primeiraFaseDias = primeiraFaseDiasHoras[0:3] #para tirar o horario e me dar somente os dias

    segundaFase = date(2022, 1, 16) #Dia da segunda fase
    segundaFaseDiasHoras = str(segundaFase - agora) # Diferença entre os dias colocados anteriormente
    segundaFaseDias = segundaFaseDiasHoras[0:3] #para tirar o horario e me dar somente os dias

    horaAgora = datetime.now()#pega o horario atual
    horario = horaAgora.strftime('%H:%M')
    print(horario+" "+primeiraFaseDias+" "+segundaFaseDias)
    # verifica se o horario atual é 11:00. Como o fuso horario do servidor é 3h adiantado, coloquei 14:00 pro bot twittar ao meio dia
    if(horario == "14:00"):
        api.update_status("Faltam " + enemDias + " dias para o enem, "+ primeiraFaseDias + " dias para a primeira fase e " + segundaFaseDias + "  dias para a segunda fase do Vestibular da Unicamp") #Tweeta
        #print("Faltam " + enemDias + " dias para o enem, "+ primeiraFaseDias + " dias para a primeira fase e " + segundaFaseDias + "  dias para a segunda fase do Vestibular da Unicamp")
        print("Deu certo")
    else:
        print("Não deu a hora ainda...")
    print("Bot running...")
    print("Faltam " + enemDias + " dias para o enem, " + primeiraFaseDias + " dias para a primeira fase e " + segundaFaseDias + "  dias para a segunda fase do Vestibular da Unicamp")
    time.sleep(15)#define o intervalo entre cada ciclo
