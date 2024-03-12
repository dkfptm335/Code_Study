def solution(players, callings):
    players_dict = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        overtake = players_dict.get(calling)
        
        players_dict[players[overtake]] -= 1
        players_dict[players[overtake-1]] += 1
        
        players[overtake], players[overtake-1] = players[overtake-1], players[overtake]
        
    return players
