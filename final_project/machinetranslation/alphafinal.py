def run():

    import os
    import json
    from dotenv import load_dotenv as load
    from ibm_watson import LanguageTranslatorV3 as ltv3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator as iama
    
    class lt:

        def __init__(self,VERSION,KEY,URL):
            self.VERSION = VERSION
            self.KEY = KEY
            self.URL = URL

        def run(self):
            self.ltv3 = ltv3(self.VERSION, iama(self.KEY))
            self.ltv3.set_service_url(self.URL)
            return self

        def tr(self,IN,LNG):
            return '\n\n'+I*9+'TRANSLATION:\n\n'+I*9+self.ltv3.translate(IN,model_id=LNG).get_result()['translations'][0]['translation'] +'\n'+ Z

        def info(self):
            return '\n\n'+I*4+'INSTANCE: '+str(self.ltv3)+'\n\n'+I*4+'VERSION: '+self.VERSION+'\n\n'+I*4+'API KEY: '+self.KEY+'\n\n'+I*4+'URL: '+self.URL+'\n'+ Z
    
    def select():
    
        while True:

            print('\n'+I*4+'CHOOSE LANGUAGE or EXIT:\n\n\n'+I*9+'ENG -> FRA [1]\n\n'+I*9+'FRA -> ENG [2]\n\n'+I*15+'EXIT [3]\n'+I*8+'_'*16+'\n')

            x = input(I*10+'SELECTION [')
            S = I*9

            if x == '1':
                print(Z +'\n\n'+I*9+'ENG -> FRA\n')
                print(LT.tr(input(S),'en-fr'))
            
            elif x == '2':
                print(Z +'\n\n'+I*9+'FRA -> ENG\n')
                print(LT.tr(input(S),'fr-en'))
            
            else:
                print(Z)
                return False

    U = '_' * 121 +'\n'
    Z = '\n' + U
    I = ' '

    load()

    VERSION = os.environ['version']
    KEY = os.environ['apikey']
    URL = os.environ['url']

    LT = lt(VERSION,KEY,URL).run()

    print(U+'\n\n'+I*4+'IBM WATSON LANGUAGE TRANSLATOR\n')
    print(U+str(LT.info()))
    
    select()

run()
