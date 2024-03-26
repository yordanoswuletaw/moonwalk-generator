from math import floor, log2
def main(n):
    round = 0
    maxRound = floor((n/2) * ((0.5 ** log2(n) - 1) / (0.5 - 1)))
    print(maxRound)
    try:
        with open('rounds.txt', 'r') as f:
            round = int(f.read().strip())
    except FileNotFoundError:
        with open('rounds.txt', 'w') as f:
            f.write(str(round))
    
    print(round, n)
    with open('rounds.txt', 'w') as f:
        f.write(str((round + 1) % maxRound))

if __name__ == '__main__':
    main(10)