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

def get_days(data, hoje, vest): #função que retorna os dias até os respectivos vestibulares
    diferenca = data - hoje
    dias = diferenca.days
    if(dias == 0): #filtragem dos possiveis valores
        return "{} Hoje!!!".format(vest)
    elif(dias < 0):
        return ""
    elif(dias == 1):
        return "{} Amanhã!!!".format(vest)
    else:
        return "{}{} dias".format(vest, dias)

agora = date.today() #Dia de hoje

#constantes com as datas dos vestibulares
ENEM = date(2021, 11, 21)
UNICAMP_PRIMEIRA_FASE = date(2021, 11, 7)
UNICAMP_SEGUNDA_FASE = date(2022, 1, 9)
FUVEST_PRIMEIRA_FASE = date(2021, 12, 12)
FUVEST_SEGUNDA_FASE = date(2022, 1, 16)

#passando os atributos para a função get_days
enem = get_days(ENEM, agora, "Enem: ") #get_days(data, hoje, vest)
unicamp_1 = get_days(UNICAMP_PRIMEIRA_FASE, agora, "Unicamp 1° fase: ") #get_days(data, hoje, vest)
unicamp_2 = get_days(UNICAMP_SEGUNDA_FASE, agora, "Unicamp 2° fase: ") #get_days(data, hoje, vest)
fuvest_1 = get_days(FUVEST_PRIMEIRA_FASE, agora, "Fuvest 1° fase: ") #get_days(data, hoje, vest)
fuvest_2 = get_days(FUVEST_SEGUNDA_FASE, agora, "Fuvest 2° fase: ") #get_days(data, hoje, vest)

#mensagem que vai ser mostrada no twitter
msg = """{}
{}
{}
{}
{}
""".format(enem, unicamp_1, unicamp_2, fuvest_1, fuvest_2) #valores que vão entrar nas {}
try:
    api.update_status(msg)
    print("deu certo")
except:
    print("error :c")
