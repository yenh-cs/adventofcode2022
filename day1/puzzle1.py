def totalCaloriesOfEachElve(data):
    totalCaloriesPerElve = []
    i = 0
    calories = 0

    while i < len(data):
        if data[i] == '\n':
            totalCaloriesPerElve.append(calories)
            calories = 0
            i += 1
            continue
        data[i] = int(data[i].strip())
        calories += data[i] 
        i += 1 

    totalCaloriesPerElve.append(calories)

    return totalCaloriesPerElve


def main():
    with open('input.txt') as f:
        data = f.readlines()
    totalCaloriesPerElve = totalCaloriesOfEachElve(data)
    max_value = max(totalCaloriesPerElve)
    print(max_value)


if __name__ == '__main__':
    main()
