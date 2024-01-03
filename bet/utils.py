import requests
from django.conf import settings

RIOT_API_KEY = settings.RIOT_API_KEY
RIOT_API_AMERICAS_URL = 'https://americas.api.riotgames.com/lol'
RIOT_API_BR_URL = 'https://br1.api.riotgames.com/lol'
headers = {'X-Riot-Token': RIOT_API_KEY}

def get_user_by_summoner_name(summoner_name):
    endpoint = f'{RIOT_API_BR_URL}/summoner/v4/summoners/by-name/{summoner_name}'
    headers = {'X-Riot-Token': RIOT_API_KEY}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        userProfile = response.json()
        return userProfile
    
    return None


def get_match_history(puuid):
    if puuid:
        match_history_endpoint = f'{RIOT_API_AMERICAS_URL}/match/v5/matches/by-puuid/{puuid}/ids'
        match_history_response = requests.get(match_history_endpoint, headers=headers)

        if match_history_response.status_code == 200:
            matches_data = match_history_response.json()

            if isinstance(matches_data, list):  # Verifica se 'matches_data' é uma lista
                return matches_data

    return None

def get_rank_stats(id):
    endpoint = f'{RIOT_API_BR_URL}/league/v4/entries/by-summoner/{id}'
    headers = {'X-Riot-Token': RIOT_API_KEY}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        rankProfile = response.json()
        return rankProfile
    
    return None


def obter_primeira_versao_ddragon():
    url_ddragon = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url_ddragon)

    if response.status_code == 200:
        versions_json = response.json()

        if versions_json:
            primeira_versao = versions_json[0]
            return primeira_versao
    else:
        print(f"Falha na solicitação. Código de status: {response.status_code}")


    return None
primeira_versao = obter_primeira_versao_ddragon()
print("Primeira versão do DDragon:", primeira_versao)

    
