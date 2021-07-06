import tweepy
from datetime import date

#tokens de acesso à conta do twitter
API_KEY = ""
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

enem = date(2021, 11, 21) #Dia da primeira fase
agora = date.today() #Dia de hoje

enemDiasHoras = str(enem - agora) # Diferença entre os dias colocados anteriormente
enemDias = enemDiasHoras[0:3] #para tirar o horario e me dar somente os dias

#unicamp********************
primeiraFase = date(2021, 11, 7) #Dia da primeira fase unicamp
primeiraFaseDiasHoras = str(primeiraFase - agora) # Diferença entre os dias colocados anteriormente
primeiraFaseDias = primeiraFaseDiasHoras[0:3] #para tirar o horario e me dar somente os dias

segundaFase = date(2022, 1, 9) #Dia da segunda fase unicamp
segundaFaseDiasHoras = str(segundaFase - agora) # Diferença entre os dias colocados anteriormente
segundaFaseDias = segundaFaseDiasHoras[0:3] #para tirar o horario e me dar somente os dias

#fuvest**********************
primeiraFaseFuvest = date(2021, 12, 12)
primeiraFaseFuvestDiasHoras = str(primeiraFaseFuvest - agora)
primeiraFaseFuvestDias = primeiraFaseFuvestDiasHoras[0:3]

segundaFaseFuvest = date(2022, 1, 16)
segundaFaseFuvestDiasHoras = str(segundaFaseFuvest - agora)
segundaFaseFuvestDias = segundaFaseFuvestDiasHoras[0:3]
msg = """
Enem: {} dias
Unicamp 1° fase: {} dias
Unicamp 2° fase: {} dias
Fuvest 1° fase: {} dias
Fuvest 2° fase: {} dias
    """.format(enemDias, primeiraFaseDias, segundaFaseDias, primeiraFaseFuvestDias, segundaFaseFuvestDias)
try:
    api.update_status(msg) #Tweeta
    print("deu certo")
except:
    print("Erro :c")