"""Track badminton Elo ratings and a simple head-to-head history."""

def expected_score(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))

def record_match(ratings, wins, winner, loser):
    ratings.setdefault(winner, 1000)
    ratings.setdefault(loser, 1000)
    change = round(32 * (1 - expected_score(ratings[winner], ratings[loser])))
    ratings[winner] += change
    ratings[loser] -= change
    wins[(winner, loser)] = wins.get((winner, loser), 0) + 1
    return change

def main():
    ratings, wins = {}, {}
    print("Badminton Elo Tracker")
    while True:
        print("\n1. Record match  2. Rankings  3. Head-to-head  4. Quit")
        choice = input("Choose: ").strip()
        if choice == "4":
            break
        if choice == "1":
            winner = input("Winner: ").strip()
            loser = input("Loser: ").strip()
            if not winner or not loser or winner.lower() == loser.lower():
                print("Use two different player names.")
                continue
            change = record_match(ratings, wins, winner, loser)
            print(f"{winner} gained {change} points; {loser} lost {change} points.")
        elif choice == "2":
            if not ratings:
                print("No matches recorded yet.")
            for name, rating in sorted(ratings.items(), key=lambda x: (-x[1], x[0])):
                print(f"{name}: {rating}")
        elif choice == "3":
            a = input("First player: ").strip()
            b = input("Second player: ").strip()
            print(f"{a} beat {b}: {wins.get((a, b), 0)} time(s)")
            print(f"{b} beat {a}: {wins.get((b, a), 0)} time(s)")
        else:
            print("Choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
