def map_instruction(game):
    instructions = { 'X': { 'A' : 'C', 'B': 'A', 'C': 'B'},
                     'Y': { 'A' : 'A', 'B': 'B', 'C': 'C'},
                     'Z': { 'A' : 'B', 'B': 'C', 'C': 'A'}
                    }

    opponent, instruction = game
    new_game = (opponent, instructions[instruction][opponent])

    return new_game


def calculate_total_score(data):
    data = [tuple(x.strip().split()) for x in data] 
    score_mapping = { 'A': 1, 'B': 2, 'C': 3 }
    instruction_result_mapping = { 'X': 0, 'Y': 3, 'Z': 6 }
    result_scores = [instruction_result_mapping[game[1]] for game in data]
    games = [map_instruction(game) for game in data]
    scores = list(map(lambda game: score_mapping[game[1]], games))
    sum_scores = [sum(i) for i in zip(result_scores, scores)]  

    return sum(sum_scores)  


def main():
    with open('input.txt') as f:
        data = f.readlines()

    total_score = calculate_total_score(data)
    print(total_score)


if __name__ == '__main__':
    main()
