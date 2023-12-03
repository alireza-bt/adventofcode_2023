"""You play several games and record the information from each game (your puzzle input). 
Each game is listed with its ID number (like the 11 in Game 11: ...) 
followed by a semicolon-separated list of subsets of cubes that were revealed from the bag 
(like 3 red, 5 green, 4 blue).
The Elf would first like to know which games would have been possible 
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?
"""
cubes_count = {'red': 12, 'green': 13, 'blue': 14}

def is_possible(game):
    if ',' in game:
        cubes_list = game.split(', ')
        for cube in cubes_list:
            if not is_possible(cube):
                return False
        return True
    else:
        item = game.split(' ')
        return int(item[0]) <= cubes_count[item[1].strip()]

with open("day2/games.txt", 'r') as f:
    sum_of_valids = 0
    for l in f:
        games = l.split(": ")
        game_id = int(games[0][5:].strip())
        sub_games = games[1].split('; ')
        game_is_possible = True
        for set in sub_games:
            if not is_possible(set):
                game_is_possible = False
                break
        if game_is_possible:
            sum_of_valids += game_id
        #print(game_id)
    print("Sum of valid game IDs: %d" % sum_of_valids)