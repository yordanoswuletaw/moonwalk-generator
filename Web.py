people = [
"Abdi Dawud Tusi",
"Chala Olani Geleta",
"Dawit Getachew Wedajo",
"Ephrem Getachew",
"Kiya Kebe Dibaba",
"Mubarak Adem Muhammed",
"Nanati Asamnew",
"Naol Kasinet",
"Fasil Hawultie",
"Dureti Mohammedsani",
"Samuel Geremew Keno",
"kaleb wondimu wotale",
"Kuma Telila",
"Biniyam Negasa Supa",
"Wondmeneh Dereje",
"---------------------------"
]
 
def round_robin_pairing(n):
    if n % 2 != 0:
        n += 1  # If the number of students is odd, add an extra student with a placeholder

    students = list(range(1, n + 1))

    # Create a list to store pairs for each day
    pairs_per_day = []

    # Generate pairs for each day
    for day in range(n - 1):
        pairs = []
        for i in range(n // 2):
            pair = (students[i], students[n - 1 - i])
            pairs.append(pair)
        pairs_per_day.append(pairs)

        # Rotate the students for the next day
        students = [students[0]] + [students[-1]] + students[1:-1]

    # If an extra student was added, remove the placeholder
    if n % 2 != 0:
        for pairs in pairs_per_day:
            pairs[-1] = (pairs[-1][0], None)

    return pairs_per_day


# Example usage with 4 students
n_students = len(people)
pairs_schedule = round_robin_pairing(n_students)

# Display the pairs for each day
# for day, pairs in enumerate(pairs_schedule, start=1):
#     for 
print("Hey **<Web/>** team,  it's time for rainwalk 🌦️ 🚶‍♀️. Find your partner below and get to know each other 😊\n")
maxRound = n_students - 2
day = 10
try:
    with open('web.txt', 'r') as f:
        round = f.read().strip()
        day = int(round) if round else 0
except FileNotFoundError:
    with open('web.txt', 'w') as f:
       f.write(str(day))

n = len(people)
count = 0
for i, j in pairs_schedule[day]:
    count+=1
    print(f'{people[i-1]} <> {people[(j-1)%n]}')
print(count)
with open('web.txt', 'w') as f:
        f.write(str((day + 1) % maxRound))