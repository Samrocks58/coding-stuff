import requests
from bs4 import BeautifulSoup


defs=[]
partsOspeech=[]
num_defs=0

def find_synonyms(word, link='https://www.thesaurus.com/browse/'):
    content = requests.get(link+ str(word)).content
    soup = BeautifulSoup(content, 'html.parser')
    synonyms=[]
    for div in soup.find_all('div'):
        try:
            if div['data-testid'] == 'word-grid-container':
                break
        except Exception:
            pass
    for li in div.find_all('li'):
        s = li.find('a').get('href').split('/browse/')[1]
        if '%20' in s:
            s = s.replace('%20', ' ')
        if '%C3%A9' in s:
            s = s.replace('%C3%A9', 'é')  
        synonyms.append(s)
    return synonyms

def find_num_definitions(word):
    global defs, partsOspeech, num_defs
    content = requests.get('https://www.thesaurus.com/browse/'+ str(word)).content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div'):
        try:
            if 'postab-container' in div.get('class'):
                num_defs = len(div.find('ul').find_all('li'))
                if num_defs == 1:
                    return 1
                elif num_defs > 1:
                    defs=[]
                    partsOspeech=[]
                    for li in div.find('ul').find_all('li'):
                        definition = li.find('a').find('strong').string
                        POS = li.find('a').find('em').string
                        defs.append(definition)
                        partsOspeech.append(POS)
                    return 2
        except Exception: pass
def find_other_definitions(word, index):
    global defs, partsOspeech, num_defs
    content = requests.get('https://www.thesaurus.com/browse/'+ str(word)).content
    soup = BeautifulSoup(content, 'html.parser')
    try:
        for sec in soup.find_all('section'):
            if 'MainContentContainer' in sec.get('class'):
                sec2 = sec.find_all('section')[0]
                deflist=[]
                ulList = sec2.find_all('ul')[1:num_defs+1]
                for li in ulList[index-1].find_all('li'):
                    s = li.find('a').get('href').split('/browse/')[1]
                    if '%20' in s:
                        s = s.replace('%20', ' ')
                    if '%C3%A9' in s:
                        s = s.replace('%C3%A9', 'é')
                    deflist.append(s)
                return deflist
    except Exception as e: pass 

word = input("Enter a word that you want synonyms of: ")
old_word = word
while not (word == 'quit' or word == 'q'):

    if find_num_definitions(word) == 1:
        print(find_synonyms(word))
    elif num_defs > 1:
        print("Which definition of the word do you want?")
        for n in range(len(defs)):
            if partsOspeech[n] != 'adj.':
                print(f"{n+1}. {partsOspeech[n]}: {defs[n]}")
            elif partsOspeech[n] == 'adj.':
                print(f"{n+1}. adjective: {defs[n]}")
        def_choice = int(input('Enter a number here: '))
        print(find_other_definitions(word, def_choice))

    word = input("Enter a new word that you want synonyms of: ")
    if word == "":
        word = old_word
    old_word = word
