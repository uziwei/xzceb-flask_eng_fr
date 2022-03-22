import json
from ibm_watson import LanguageTranslatorV3 as ltv3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as iama
import os
from dotenv import load_dotenv as load

load()

VERSION = os.environ['version']
KEY = os.environ['apikey']
URL = os.environ['url']

print('_________________________________________________________________________________________________________________________\n\n\n    IBM WATSON LANGUAGE TRANSLATOR\n\n_________________________________________________________________________________________________________________________')

def select(x):
    
    y = lt(VERSION,KEY,URL).run()
    
    if x == '1':
        print('\n_________________________________________________________________________________________________________________________\n\n\n    ENG -> FRA\n')
        return y.tr(input('    '),'en-fr')
    
    elif x == '2':
        print('\n_________________________________________________________________________________________________________________________\n\n\n    FRA -> ENG\n')
        return y.tr(input('    '),'fr-en')
    
    else:
         print('\n_________________________________________________________________________________________________________________________\n')
         None

def check(x):
    if x == 'C' or x == 'c':
        X = lt(VERSION,KEY,URL).run()
        print('\n_________________________________________________________________________________________________________________________\n'+str(X.info()))
    else:
        print('\n_________________________________________________________________________________________________________________________\n')

class lt:

    def __init__(self,VERSION,KEY,URL):
        self.VERSION = VERSION
        self.KEY = KEY
        self.URL = URL


    def run(self):
        self.ltv3 = ltv3(self.VERSION, iama(self.KEY))
        self.ltv3.set_service_url(self.URL)
        return self
    # Creates ltv3 object w/ VERSION n KEY parameters and calls .set_service_url(URL parameter) method

    def tr(self,IN,LNG):
        return '\n\n    TRANSLATION:\n\n'+'    '+self.ltv3.translate(IN,model_id=LNG).get_result()['translations'][0]['translation'] +'\n\n_________________________________________________________________________________________________________________________\n'

    def info(self):
        return '\n\n'+'    INSTANCE: '+str(self.ltv3)+'\n\n'+'    VERSION: '+self.VERSION+'\n\n'+'    '+'API KEY: '+self.KEY+'\n\n'+'    '+'URL: '+self.URL+'\n\n_________________________________________________________________________________________________________________________\n'




# creates ltv3 object


print('\n\n    Enter C to CHECK \n')


check(input('    '))


print('\n    CHOOSE LANGUAGE or EXIT:\n\n              ENG -> FRA [1]\n\n              FRA -> ENG [2]\n\n                    EXIT [3]\n             ________________\n')




print(select(input('               SELECTION [')))







# all in one fucker