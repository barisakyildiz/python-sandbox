def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def my_reduce(func, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = func(result, item)
    return result

def total():
    exercise_dicti = {}

    def process_line(line):
        line = line.strip().split(";")
        for i in range(3, len(line)):
            try:
                temp = line[i]
                exercise_dicti[line[0]] += 1
            except KeyError:
                exercise_dicti[line[0]] = 1
            except Exception:
                exercise_dicti[line[0]] -= 1
                break

    with open("sport.csv", "r") as file:
        my_map(process_line, file)

    print(exercise_dicti)


def bestWorst():
    dicti = {}

    def process_line(line):
        line = line.strip().split(";")
        best = float(line[3])
        worst = float(line[3])
        name = line[0]
        sport = line[2]
        line.pop(-1)
        for j in range(3, len(line)):
            if float(line[j]) <= best:
                best = float(line[j])
            elif float(line[j]) >= worst:
                worst = float(line[j])
        emStr = "{} {}".format(line[0], line[2])
        bsStr = "{} {}".format(best, worst)
        dicti[emStr] = bsStr

    with open("sport.csv", "r") as file:
        lines = file.readlines()
        my_map(process_line, lines)

    print(dicti)


def main():
    total()  # Returns the total number of exercises
    print("\n\n\n")
    bestWorst()  # Returns the best and worst results for each person in each sport


if __name__ == '__main__':
    main()