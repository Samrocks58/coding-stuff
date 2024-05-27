import requests
from bs4 import BeautifulSoup

defs=[]
partsOspeech=[]
synonymCards = []
num_defs=0

def find_num_definitions(word):
    global defs, partsOspeech, num_defs, synonymCards
    content = requests.get('https://www.thesaurus.com/browse/'+ str(word)).content
    soup = BeautifulSoup(content, 'html.parser')
    for sec in soup.find_all('section'):
        try:
            if sec['data-type'] == 'synonym-antonym-module':
                    for d in sec.find_all('div'):
                        if 'data-type' in list(d.attrs.keys()):
                            if d['data-type'] == 'synonym-and-antonym-card':
                                synonymCards.append(d)
                                for d2 in d.find_all('div'):
                                    if d2.p != None:
                                        if 'id' in list(d2.p.attrs.keys()):
                                            defState = d2.p.get_text().replace("\"", "").split()
                                            defState.remove('as')
                                            defState.remove('in')
                                            POS = defState[0]
                                            Defstr = ""
                                            for i in defState[1:]:
                                                Defstr += i + " "
                                            # print(POS)
                                            # print(Defstr)
                                            defs.append(Defstr)
                                            num_defs += 1
                                            partsOspeech.append(POS)
        except Exception:
            pass

def find_definitions(index):
    global num_defs, synonymCards

    s = synonymCards[index-1]
    wordList = []
    body = s.find_all('div')[1]
    body2 = body.find_all('div')[1]
    for d in body2.find_all('div'):
        if (d.find('p').get_text() == "Strongest matches") or (d.find('p').get_text() == "Strong matches"):
            ul = d.find('ul')
            for li in ul.find_all('li'):
                wordList.append(li.get_text())
    return wordList

word = input("Enter a word that you want synonyms of: ")
word = "bad"
old_word = word
while not (word == 'quit' or word == 'q'):

    if find_num_definitions(word) == 1:
        print(find_definitions(1))
    elif num_defs > 1:
        print("Which definition of the word do you want?")
        for n in range(len(defs)):
            if partsOspeech[n] != 'adj.':
                print(f"{n+1}. {partsOspeech[n]}: {defs[n]}")
            elif partsOspeech[n] == 'adj.':
                print(f"{n+1}. adjective: {defs[n]}")
        def_choice = int(input('Enter a number here: '))
        print(find_definitions(def_choice))
        
    word = input("Enter a new word that you want synonyms of: ")
    if word == "":
        word = old_word
    old_word = word
