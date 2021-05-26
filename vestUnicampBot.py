import tweepy
from datetime import datetime, date
import os
from os import environ
import time

while True :#rotina para o codigo atualizar a cada 15 segundos
    #tokens de acesso à conta do twitter
    API_KEY = environ['API_KEY']
    API_SECRET_KEY = environ['API_SECRET_KEY']
    ACCESS_TOKEN = environ['ACCESS_TOKEN']
    ACCESS_SECRET_TOKEN = environ['ACCESS_SECRET_TOKEN']

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    api = tweepy.API(auth)

    primeiraFase = date(2021, 11, 21) #Dia da primeira fase
    agora = date.today() #Dia de hoje

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
        api.update_status("Faltam " + primeiraFaseDias + " dias para a primeira fase e " + segundaFaseDias + " dias para a segunda fase do Vestibular da Unicamp") #Tweeta
        print("Faltam " + primeiraFaseDias + " dias para a primeira fase e " + segundaFaseDias + " dias para a segunda fase do Vestibular da Unicamp")
        print("Deu certo")
    else:
        print("Não deu a hora ainda...")
    print("Bot running...")
    time.sleep(15)#define o intervalo entre cada ciclo
