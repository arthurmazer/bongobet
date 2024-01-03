from django.shortcuts import render
from .utils import get_match_history
from .utils import get_user_by_summoner_name
from .utils import get_rank_stats
from .utils import obter_primeira_versao_ddragon
import math

# Create your views here.
def render_view_index(request):
    return render(request, 'index.html')

def render_view_bet_lol(request):
    summonerName = request.GET.get('summonerName', '')
    userProfile = get_user_by_summoner_name(summonerName)
    puuid = userProfile.get('puuid')
    id = userProfile.get('id')
    match_history = get_match_history(puuid)
    rankProfile = get_rank_stats(id)

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


    context = {
        'iconRankSolo': iconRankSolo,
        'iconRankFlex': iconRankFlex,
        'summonerName': summonerName, 
        'userProfile' : userProfile, 
        'matchHistory': match_history,
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

    print(summonerName)
    print(userProfile)
    print(match_history)
    print(solo_rank)
    print(flex_rank)
    print(lolLastVersion)
    print(rankProfile)
    return render(request, 'lolbet.html', context)



