# Create a program in which the user creates 
# a specific FRC team and store the following variables:
	# Team Number (named team_number)
	# Team Name (named team_name)
	# Location (named location)
	# Rookie Year (named rookie_year)
	# Is Active (named is_active)
# Be sure to store each variable as the correct type!
team_number = str(input("What is the team number? "))
team_name = str(input("What is the team name? "))
location = input("Where is the team located? ")
rookie_year = int(input("What year was the team started? "))
is_active = bool(input("Is the team still active? "))
print(team_number)
print(team_name)
print(location)
print(rookie_year)
print(is_active)
print("Team", team_name, "aka as", team_number,"is based in",location, "and was started in the year",rookie_year)
if is_active == True:
    print("Still Active: ", True)
else:
    print("Still Active: ", False)