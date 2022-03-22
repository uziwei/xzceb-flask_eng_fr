import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

VERSION='2018-05-01'

AUTH = IAMAuthenticator(APIKEY)
translator_instance = LanguageTranslatorV3(version=VERSION,authenticator=AUTH)
translator_instance.set_service_url(URL)
translator_instance

from pandas import json_normalize

json_normalize(translator_instance.list_identifiable_languages().get_result(), "languages")



def englishToFrench(englishText):
    #write the code here
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    return englishText