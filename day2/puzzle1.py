def calculate_score_on_a_game(game):
   opponent, me = game
   diff = ord(me) - ord(opponent)
   score = 3
   if diff == 22 or diff == 25:
       score = 0
   elif diff == 21 or diff == 24:
       score = 6 
   
   return score 


def calculate_total_score(data):
    data = [tuple(x.strip().split()) for x in data] 
    score_mapping = { 'X': 1, 'Y': 2, 'Z': 3 }
    scores = list(map(lambda game: score_mapping[game[1]] + calculate_score_on_a_game(game), data))

    return sum(scores)  


def main():
    with open('input.txt') as f:
        data = f.readlines()

    total_score = calculate_total_score(data)
    print(total_score)

if __name__ == '__main__':
    main()
