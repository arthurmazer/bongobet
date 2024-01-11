from django.shortcuts import render
from .utils import get_match_history
from .utils import get_user_by_summoner_name
from .utils import get_rank_stats
from .utils import obter_primeira_versao_ddragon
from .utils import get_queue_json
from datetime import datetime, timedelta
import math

# Create your views here.
def render_view_index(request):
    return render(request, 'index.html')

def render_view_bet_lol(request):
    summonerName = request.GET.get('summonerName', '')
    userProfile = get_user_by_summoner_name(summonerName)
    puuid = userProfile.get('puuid')
    id = userProfile.get('id')
    
    rankProfile = get_rank_stats(id)
    queueJson = get_queue_json()

    solo_rank = None
    flex_rank = None
    iconRankFlex = 'Unranked.png'
    iconRankSolo = 'Unranked.png'
    winsSolo = 0
    lossesSolo = 0
    partidasSolo = 0
    winsFlex = 0
    lossesFlex = 0
    partidasFlex = 0
    winrateSolo = 0
    winrateFlex = 0

    for result in rankProfile:
        if 'queueType' in result and result['queueType'] == 'RANKED_SOLO_5x5':
            solo_rank = str(result.get('tier')).capitalize() + ' ' +  str(result.get('rank')) + ' - ' + str(result.get('leaguePoints')) + ' pdl'
            iconRankSolo = str(result.get('tier')).lower() + '.png'
            winsSolo = result.get('wins')
            lossesSolo = result.get('losses')
            partidasSolo = winsSolo + lossesSolo
            winrateSolo = math.floor((winsSolo/partidasSolo)*100)
        elif 'queueType' in result and result['queueType'] == 'RANKED_FLEX_SR':
            flex_rank = str(result.get('tier')).capitalize() + ' ' + str(result.get('rank')) + ' - ' + str(result.get('leaguePoints')) + ' pdl'
            iconRankFlex = str(result.get('tier')).lower() + '.png'
            winsFlex = result.get('wins')
            lossesFlex = result.get('losses')
            partidasFlex = winsFlex + lossesFlex
            winrateFlex = math.floor((winsFlex /partidasFlex)*100)

    lolLastVersion = obter_primeira_versao_ddragon()
    profileIconId = userProfile.get('profileIconId')
    urlProfileImg = 'https://ddragon.leagueoflegends.com/cdn/' + str(lolLastVersion) + '/img/profileicon/' + str(profileIconId) + '.png'

    # Match History

    #Carrega da API as 10 ultimas partidas
    match_history = get_match_history(puuid)

    myMatchhistory = []
    #prepara os dados para serem exibidos na view
    for match in match_history:
        queueId = match.get('info').get('queueId')
        filtered_queues = [queue for queue in queueJson if queue["queueId"] == queueId]

        #gameType = RANKED SOLO 5x5 , RANKED_FLEX_SR etc...
        gameType = filtered_queues[0].get('description')

        # --------- Game Date ------------
        # e.g 3 Dias atrás
        gameStartTime = match.get('info').get('gameStartTimestamp')
        gameEndTime = match.get('info').get('gameEndTimestamp')
        
        game_end_time = datetime.fromtimestamp(gameEndTime / 1000.0)

        # Obtenha a diferença em dias
        diff = datetime.now() - game_end_time
        diff_months = diff.days // 30
        diff_years = diff.days // 365
        diff_hours = diff.seconds // 3600

        time_string = ""
        if diff_years > 0:
            time_string = f"Há {diff_years} anos atrás"
        elif diff_months > 0:
            if diff_months == 1:
                time_string = f"{diff_months} mês atrás"
            else:
                time_string = f"{diff_months} meses atrás"
        elif diff.days > 0:
            if diff.days == 1:
                time_string = f"{diff.days} dia atrás"
            else:
                time_string = f"{diff.days} dias atrás"
        else:
            if diff_hours == 1:
                time_string = f"{diff_hours} hora atrás"
            else:
                time_string = f"{diff_hours} horas atrás"


        # --------- Game Duration ------------
        gameDuration = gameEndTime - gameStartTime
        # Converta para segundos
        gameDuration_in_seconds = gameDuration / 1000

        # Calcule minutos e segundos
        minutes = int(gameDuration_in_seconds // 60)
        seconds = int(gameDuration_in_seconds % 60)

        # Formate a string
        duration_string = f"{minutes}m {seconds}s"

        # --------- Match Result  ------------
        # e.g Vitoria
        participants = match.get('info').get('participants') if match_history else []
        myPlayer = list(filter(lambda p: p.get("summonerName") == summonerName, participants))

        win = myPlayer[0]["win"]
        result = "Vitória" if win else "Derrota"

        # --------- Champion Details  ------------
        # e.g Garen
        championId = myPlayer[0]["championId"]
        championName = myPlayer[0]["championName"]
        championLevel = myPlayer[0]["champLevel"]
        championImg = f'https://ddragon.leagueoflegends.com/cdn/{lolLastVersion}/img/champion/{championName}.png'
        kills = myPlayer[0]["kills"]
        deaths = myPlayer[0]["deaths"] 
        assists = myPlayer[0]["assists"]
        kda = f'{kills} / {deaths} / {assists}'
        kdaRatio = myPlayer[0]["challenges"]["kda"]
        killParticipation = int(myPlayer[0]["challenges"]["killParticipation"]*100)
        multikills = myPlayer[0]["challenges"]["multikills"]
        soloKills = myPlayer[0]["challenges"]["soloKills"]
        killingSprees = myPlayer[0]["killingSprees"]
        item0 = myPlayer[0]["item0"]
        item1 = myPlayer[0]["item1"]
        item2 = myPlayer[0]["item2"]
        item3 = myPlayer[0]["item3"]
        item4 = myPlayer[0]["item4"]
        item5 = myPlayer[0]["item5"]
        trinket = myPlayer[0]["item6"] 
        lanePlayed = myPlayer[0]["lane"]
        controlWardsPlaced = myPlayer[0]["challenges"]["controlWardsPlaced"]
        totalMinionsKilled = myPlayer[0]["totalMinionsKilled"]

        # --------- Teams  ------------
        teams = []
        for players in participants:
            playerName = players["summonerName"]
            championPlayed = players["championName"]
            champImg = f'https://ddragon.leagueoflegends.com/cdn/{lolLastVersion}/img/champion/{championPlayed}.png'

            teams.append({
                "playerName": playerName,
                "champImg": champImg,
                "championPlayed": championPlayed
            })


        myMatchhistory.append({
            "gameType": gameType,
            "time_string": time_string,
            "duration_string": duration_string,
            "result": result,
            "championId": championId,
            "championName": championName,
            "championLevel": championLevel,
            "championImg": championImg,
            "kda": kda,
            "kills": kills,
            "assists": assists,
            "deaths": deaths,
            "kdaRatio": kdaRatio,
            "killParticipation": killParticipation,
            "multikills": multikills,
            "soloKills": soloKills,
            "killingSprees": killingSprees,
            "item0": item0,
            "item1": item1,
            "item2": item2,
            "item3": item3,
            "item4": item4,
            "item5": item5,
            "trinket": trinket,
            "lanePlayed": lanePlayed,
            "teams": teams,
            "controlWardsPlaced": controlWardsPlaced,
            "totalMinionsKilled": totalMinionsKilled,
            "win": win
        })

        #END FOR Match History

    context = {
        'iconRankSolo': iconRankSolo,
        'iconRankFlex': iconRankFlex,
        'summonerName': summonerName, 
        'userProfile' : userProfile, 
        'matchHistory': myMatchhistory,
        'soloRanked': solo_rank, 
        'flexRank': flex_rank,
        'urlProfileImg': urlProfileImg,
        'winsSolo': winsSolo, 
        'lossesSolo': lossesSolo,
        'winrateSolo': winrateSolo,
        'winsFlex': winsFlex, 
        'lossesFlex': lossesFlex,
        'winrateFlex': winrateFlex,
        'partidasSolo': partidasSolo,
        'partidasFlex': partidasFlex
    }
    return render(request, 'lolbet.html', context)


