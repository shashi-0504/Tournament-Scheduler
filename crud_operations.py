from abstraction import abstraction
from datetime import datetime
from tabulate import tabulate

class MatchScheduler:
    def __init__(self):
        self.matches = []

    def generate_matches(self, teams):
        self.matches = []
        match_id = 1
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                self.matches.append({"id": match_id, "teams": [teams[i], teams[j]]})
                match_id += 1
        print("Matches generated successfully!")

    def schedule_matches(self):
        if not self.matches:
            print("No matches available to schedule.")
            return

        print("\nLet's schedule the matches. Enter the date and time for each match.")
        for match in self.matches:
            print(f"\nMatch ID: {match['id']}, Teams: {match['teams'][0]} vs {match['teams'][1]}")
            while True:
                date = input("Enter match date (YYYY-MM-DD): ").strip()
                time = input("Enter match time (HH:MM): ").strip()
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    datetime.strptime(time, "%H:%M")
                    match["date"] = date
                    match["time"] = time
                    break
                except ValueError:
                    print("Invalid date or time format. Please try again.")
        print("All matches have been scheduled successfully! 👍👍")

    def view_matches(self):
        if not self.matches:
            print("No matches scheduled.")
        else:
            headers = ["ID", "Teams", "Date", "Time"]
            table = [
                [match["id"], f"{match['teams'][0]} vs {match['teams'][1]}", match.get("date", "Not Scheduled"),
                 match.get("time", "Not Scheduled")]
                for match in self.matches
            ]
            print("\nMatch Schedule:")
            print(tabulate(table, headers=headers, tablefmt="grid"))

    def update_match(self):
        if not self.matches:
            print("No matches to update.")
            return

        try:
            match_id = int(input("Enter the Match ID to update: ").strip())
        except ValueError:
            print("Invalid ID. Please enter a valid number.")
            return

        for match in self.matches:
            if match["id"] == match_id:
                print(f"\nCurrent Details for Match ID {match_id}: Teams: {match['teams'][0]} vs {match['teams'][1]}, "
                      f"Date: {match.get('date', 'Not Scheduled')}, Time: {match.get('time', 'Not Scheduled')}")
                while True:
                    date = input("Enter new match date (YYYY-MM-DD): ").strip()
                    time = input("Enter new match time (HH:MM): ").strip()
                    try:
                        datetime.strptime(date, "%Y-%m-%d")
                        datetime.strptime(time, "%H:%M")
                        match["date"] = date
                        match["time"] = time
                        print("Match updated successfully!")
                        return
                    except ValueError:
                        print("Invalid date or time format. Please try again.")
        print("Match not found.")

    def cancel_match(self):
        if not self.matches:
            print("No matches to cancel.")
            return

        try:
            match_id = int(input("Enter the Match ID to cancel: ").strip())
        except ValueError:
            print("Invalid ID. Please enter a valid number.")
            return

        for match in self.matches:
            if match["id"] == match_id:
                print(f"\nMatch ID: {match_id}, Teams: {match['teams'][0]} vs {match['teams'][1]}")
                weather = input("What is the weather like? (Sunny/Rainy/Cloudy): ").strip().lower()
                if weather == "rainy":
                    self.matches.remove(match)
                    print(f"Match ID {match_id} canceled due to rainy weather! 🌧️")
                else:
                    print("The match can continue. No cancellation required. ☀️")
                return
        print("Match not found.")

    def check_conflicts(self):
        if not self.matches:
            print("No matches scheduled.")
            return

        conflicts = []
        match_schedule = {}

        for match in self.matches:
            if "date" in match and "time" in match:
                key = (match["date"], match["time"])
                if key not in match_schedule:
                    match_schedule[key] = []
                match_schedule[key].append(match)

        for key, conflict_matches in match_schedule.items():
            if len(conflict_matches) > 1:
                conflicts.append((key, conflict_matches))

        if conflicts:
            print("\nConflicts Found:")
            for (date, time), conflict_matches in conflicts:
                print(f"\nDate: {date}, Time: {time}")
                for conflict in conflict_matches:
                    print(f"  Match ID: {conflict['id']}, Teams: {conflict['teams'][0]} vs {conflict['teams'][1]}")
        else:
            print("No conflicts found. All matches are scheduled properly.")



