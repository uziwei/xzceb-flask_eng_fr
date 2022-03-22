import json
from ibm_watson import LanguageTranslatorV3 as ltv3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as iama

import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ['apikey']
URL = os.environ['url']

LT = ltv3('2018-05-01',iama(KEY))

LT.set_service_url(URL)

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