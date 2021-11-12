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

agora = date.today() #Dia de hoje

def get_days(data, vest): #função que retorna os dias até os respectivos vestibulares
    diferenca = data - agora
    dias = diferenca.days
    if(dias == 0): #filtragem dos possiveis valores
        return "{} Hoje!!!".format(vest)
    elif(dias < 0):
        return ""
    elif(dias == 1):
        return "{} Amanhã!!!".format(vest)
    else:
        return "{}{} dias".format(vest, dias)

#get_days((data do vestibular), (mensagem do vestibular))
enem = get_days(date(2021, 11, 21), "Enem: ")
unicamp_1 = get_days(date(2021, 11, 7), "Unicamp 1° fase: ")
unicamp_2 = get_days(date(2022, 1, 9), "Unicamp 2° fase: ")
fuvest_1 = get_days(date(2021, 12, 12), "Fuvest 1° fase: ")
fuvest_2 = get_days(date(2022, 1, 16), "Fuvest 2° fase: ")
unesp_1 = get_days(date(2021, 11, 14), "Unesp 1° fase: ")
unesp_2 = get_days(date(2021, 12, 19), "Unesp 2° fase: ")

#mensagem que vai ser mostrada no twitter
msg = """{}
{}
{}
{}
{}
{}
{}
""".format(enem, unicamp_1, unicamp_2, fuvest_1, fuvest_2, unesp_1, unesp_2) #valores que vão entrar nas {}
try:
    #api.update_status(msg)
    print(msg)
    print("deu certo")
except:
    print("error :c")