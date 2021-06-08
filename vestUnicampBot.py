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
    print(horario+" "+primeiraFaseDias+" "+segundaFaseDias + " " + enemDias)

    #define a mensagem do tweet
    msg = """
Enem: {} dias
Unicamp 1° fase: {} dias
Unicamp 2° fase: {} dias
    """.format(enemDias, primeiraFaseDias, segundaFaseDias)
    # verifica se o horario atual é 11:00. Como o fuso horario do servidor é 3h adiantado, coloquei 14:00 pro bot twittar ao meio dia
    if(horario == "14:06"):
        try:#não deixa a aplicação morrer quando acontecer erros no servidor
            api.update_status(msg) #Tweeta
            print("Deu certo")
        except:
            print("Esse tweet ja existe :c")
    else:
        print("Não deu a hora ainda...")
    print("Bot running...")
    print(msg)
    time.sleep(15)#define o intervalo entre cada  ciclo
