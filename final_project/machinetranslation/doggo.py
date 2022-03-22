import json
from ibm_watson import LanguageTranslatorV3 as ltv3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as iama
import os
from dotenv import load_dotenv as load

load()

VERSION = os.environ['version']
KEY = os.environ['apikey']
URL = os.environ['url']

class lt:

    def __init__(self,VERSION,KEY,URL):
        self.VERSION = VERSION
        self.KEY = KEY
        self.URL = URL


    def run(self):
        x = ltv3(self.VERSION, iama(self.KEY))
        x.set_service_url(self.URL)
        return x
    # Creates ltv3 object w/ VERSION n KEY parameters and calls .set_service_url(URL parameter) method


    def info(self):
        return self.VERSION+'\n\n'+self.KEY+'\n\n'+self.URL


X = lt(VERSION,KEY,URL)


C = '\n'+str(X.run())+'\n\n'+str(X.info())+'\n\n'+str(type(X.run()))+'\n'


print(lt(VERSION,KEY,URL).run())




