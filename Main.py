from crud_operations import MatchScheduler

class TournamentManager:
    def __init__(self):
        self.scheduler = MatchScheduler()

    def main_menu(self):
        print("\n........ 🏆 WELCOME TO THE TOURNAMENT 🏆 ........\n")
        while True:
            print("----------------------------------------------------")
            print("1. Add Teams and Generate Matches 👥")
            print("2. Schedule Matches 🗓️")
            print("3. View Matches 👁️‍🗨️")
            print("4. Update Match 🔄")
            print("5. Cancel Match ❌")
            print("6. Check for Conflicts ⚠️")
            print("7. Exit ↩")
            print("----------------------------------------------------")

            choice = input("Choose an option: ").strip()
            print("----------------------------------------------------")

            if choice == "1":
                self.add_teams_and_generate_matches()
            elif choice == "2":
                self.scheduler.schedule_matches()
            elif choice == "3":
                self.scheduler.view_matches()
            elif choice == "4":
                self.scheduler.update_match()
            elif choice == "5":
                self.scheduler.cancel_match()
            elif choice == "6":
                self.scheduler.check_conflicts()
            elif choice == "7":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def add_teams_and_generate_matches(self):
        try:
            num_teams = int(input("Enter the number of teams: ").strip())
            if num_teams < 2:
                print("At least 2 teams are required to generate matches.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        teams = []
        for i in range(num_teams):
            team_name = input(f"Enter name of team {i + 1}: ").strip()
            teams.append(team_name)
        self.scheduler.generate_matches(teams)

        print(f"\nGenerated {len(self.scheduler.matches)} matches:")
        for match in self.scheduler.matches:
            print(f"Match ID: {match['id']}, Teams: {match['teams'][0]} vs {match['teams'][1]}")

# Example Usage
if __name__ == "__main__":
    manager = TournamentManager()
    manager.main_menu()
