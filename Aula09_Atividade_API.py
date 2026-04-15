import requests
import pandas as pd

def pegaLocViaAPI():
    try:
        # Faz a requisição para a API
        requestLoc = requests.get('https://ipinfo.io/json', timeout=10)
        requestLoc.raise_for_status()  # Levanta exceção para status de erro
        
        data = requestLoc.json()
        
        # As coordenadas vêm como "lat,long" em uma unica string
        loc = data.get('loc', '').split(',')
        
        location_info = {
            
            'city': data.get('city'),
            'latitude': float(loc[0]) if len(loc) > 0 else None,
            'longitude': float(loc[1]) if len(loc) > 1 else None,
        }
        
        return location_info
    
    except requests.exceptions.RequestException as e: #mostra qualquer exeção que pode ocorrer
        print(f"Erro na requisição: {e}")
        return None

localizacao = pegaLocViaAPI()#aqui coloca os dados numa variavel para ser utilizada
latitude = localizacao['latitude']
longitude = localizacao['longitude']

def API_Clima():

    requestWheater = 'https://api.open-meteo.com/v1/forecast'
    parametrosClima = {
	"latitude": latitude,
	"longitude": longitude,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m"],
	"forecast_days": 7, 
    "timezone": "auto"
    }
    

    resposta = requests.get(requestWheater, params=parametrosClima)

    if resposta.status_code == 200:#verifica se tem resposta da requisição do site
        
        dados = resposta.json()

        # Extrair os dados horários corretamente (acesso direto ao JSON)
        hourly_data = {
            "Date": pd.to_datetime(dados['hourly']['time']),
            "Temperature_Celsius": dados['hourly']['temperature_2m'],
            "Relative humidity": dados['hourly']['relative_humidity_2m'],
            "Precipitation": dados['hourly']['precipitation'],
            "wind_Speed": dados['hourly']['wind_speed_10m'],

        }

        df_completo = pd.DataFrame(data=hourly_data)#dataFrame com todos os dados
        df_completo['Temperature_Fahrenheit '] = df_completo['Temperature_Celsius'] * 1.8 + 32 #adciona a tabela com temperatura convertida
        
        # 1. Dia de hoje
        hoje = pd.Timestamp.now().normalize()  #Pega e Normaliza os dados de Hoje a partir das 00h
        #remove os itens da tabela que não pertence a "Hoje"
        df_hoje = df_completo[df_completo['Date'] >= hoje]
        df_hoje = df_hoje[df_hoje['Date'] < hoje + pd.Timedelta(days=1)]
        
        print(f"\nDados climáticos de {localizacao['city']} obtidos!") #mostra a localização da API que pega a Lat e long 
        print(f"\nClima de hoje:")
        print(df_hoje)
        print(f"\n")
        print(f"\nCLima da semana:")
        print(df_completo)
        print(f"\n")
        df_hoje.to_csv("Clima de Hoje.csv", index=False)
        df_completo.to_csv("Clima da Semana.csv", index=False)
        
    # se a api caiu ou nao funciona
    else:
        print(f'Erro ao acessar a API - {resposta.status_code}')

API_Clima()

