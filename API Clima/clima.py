class clima_API:

    def __init__(self, clima):
        clima = str(clima)
        if self.clima_temp(clima):
            self.clima = clima
        else:
            raise ValueError("Clima não !")
    
    def __str__(self):
        return self.__format__clima()
    
    def clima_temp(self, clima):
        if len(clima) == 6:
            return True
        else:
            return False
    
    def format_cep(self):
        return "{}-{}".format(self.clima[:5],self.clima[5:])

    def acessa_api(self):
        url_previsao = "https://api.hgbrasil.com/weather?key=e1a836da&lat=-23.682&log=-46.875&user_ip=remote/ws/{}/json".format(self.clima)
        url = "http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a954d7f6fd425daba5fe25ec979f8d9f/ws/{}/json/".format(self.clima)
        print(url_previsao)
        print(url)
