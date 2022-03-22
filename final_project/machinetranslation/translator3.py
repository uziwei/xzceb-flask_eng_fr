import json
from ibm_watson import LanguageTranslatorV3 as ltv3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as iama
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ['apikey']
URL = os.environ['url']
# uses OS env system to hide keys???

TOKEN = iama(KEY)
# creates TOKEN usin API key

LT = ltv3('2018-05-01',TOKEN)
# creates LT which is language translator instance/ object

LT.set_service_url(URL)
# URL method set on LT object


print(str(type(LT)) +'\n')
# should print <class 'ibm_watson.language_translator_v3.LanguageTranslatorV3'> as a string and add line space

print('EN->FR \n')

INPUT = input()
# input deasired text to translate

translation = LT.translate(text=INPUT, model_id='en-fr').get_result()
# method to translate LT -> ENG to FR

print('\n'+ translation['translations'][0]['translation'] +'\n')
# prints specifically translation output

print('FR->EN \n')

INPUT1 = input()
# input deasired text to translate

translation1 = LT.translate(text=INPUT1, model_id='fr-en').get_result()
# method to translate LT -> FR to ENG

print('\n'+ translation1['translations'][0]['translation'] +'\n')
# prints specifically translation1 output