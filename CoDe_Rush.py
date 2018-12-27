
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests
import webbrowser

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def start_skill():
    welcome_message = 'Hallo zur Baur-App. Nach was soll ich suchen?'
    return question(welcome_message)
    
@ask.intent("SuchAbfrage", mapping={'Produkt':'Produkt', 'filter1': 'Filter_color'})
def search_Produkt(Produkt, filter1):    
    print(filter1)
    print(Produkt)
    color = 'f11111'

    if filter1[0:7] =='schwarz':
        color='black'
    elif filter1[0:3]=='rot' or filter1==None:
        color='red'
    elif filter1[0:4]=='blau':
        color='blue'
    elif filter1[0:9]=='edelstahl':
        Produkt = filter1 + Produkt
        color=''
    elif filter1[0:4]=='grün':
        color='green'
    elif filter1[0:4]=='gelb': 
        color='yellow'  
    
    url_main = 'https://www.baur.de/suche/serp/magellan?'
    url_query = 'query='+ Produkt+'&amp;start=72&amp;locale=de_DE&amp;count=24&amp;clientId=BaurDe&amp;'
    url_filter = 'filterValues=filter_color%3D'+'f52'+'&color='+color
    if Produkt in ('schuhe', 'sportschuhe'):
        url_filter = url_filter + '&size=' + '41' 
    url_end = '&amp;order=price-asc'
    url = url_main+url_query+url_filter+url_end
    print(url)
    response = requests.get(url)
    data = response.json()
    
    liste=[]    
    liste.append(data["searchresult"]["result"]["styles"][0]["price"]["value"])
    liste.append(data["searchresult"]["result"]["styles"][0]['name'])
    liste.append(data["searchresult"]["request"]["sortType"])
    liste.append(data["searchresult"]["result"]["count"])
    liste.append(data["searchresult"]["result"]["styles"][0]["name"])
    
    beschreibung = liste[1]
    intpos = [len(beschreibung)]
    for i in ['(',')']:
        intpos.append(beschreibung.find(i))
    beschreibung = beschreibung[0:min(intpos)]
    Message = 'Die Suche nach ' + Produkt + ' hat ' + beschreibung +' ergeben und kostet '  + str(liste[0])+'€'
    
    art_nr = data['searchresult']['result']['styles'][0]
    art_nr = art_nr['sku']
    art_nr = art_nr[0:art_nr.find('-')]

    webbrowser.open("https://www.baur.de/s/"+art_nr)
    return question(Message)
    
@ask.intent("ThanksIntent")
def dankeAlexa():
    Message = 'Bitteschön. '
    return question(Message)

@ask.intent("Ciao")
def Ciao():
    Message = 'Bis bald. PS: Wählt daffd - Sie sind sehr gut'
    return question(Message)

if __name__ == '__main__':
    app.run(debug=True)
