"""--- Part Two ---

As you continue your walk, the Elf poses a second question: 
in each game you played, what is the fewest number of cubes of each color 
that could have been in the bag to make the game possible?
"""
min_possible_cubes = {'red': 0, 'green': 0, 'blue': 0}

def find_min_possible_cubes(game):
    if ',' in game:
        cubes_list = game.split(', ')
        for cube in cubes_list:
            find_min_possible_cubes(cube)
    else:
        item = game.split(' ')
        if int(item[0]) > min_possible_cubes[item[1].strip()]:
            min_possible_cubes[item[1].strip()] = int(item[0])

with open("day2/games.txt", 'r') as f:
    total_power = 0
    for l in f:
        games = l.split(": ")
        game_id = int(games[0][5:].strip())
        sub_games = games[1].split('; ')
        # make all of them zero
        min_possible_cubes['blue'] = 0
        min_possible_cubes['red'] = 0
        min_possible_cubes['green'] = 0
        # then fill with the max value from the games
        for set in sub_games:
            find_min_possible_cubes(set)
        #print(min_possible_cubes)
        total_power += (min_possible_cubes['blue']*min_possible_cubes['red']*min_possible_cubes['green'])
    print("Sum of valid game IDs: %d" % total_power)