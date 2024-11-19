
print("SURVEY")
computerScience = input("Are you interested in computer science? (y/n)")
computerGames = input("Do you like playing computer games? (y/n)")
instagramAcc = input("Do you have an Instagram account? (y/n)")



if computerScience == 'y':
    computerScience = True
else:
    computerScience = False

if computerGames == 'y':
    computerGames = True
else:
    computerGames = False

if instagramAcc == 'y':
    instagramAcc = True
else:
    instagramAcc = False

print("SURVEY RESULTS")
print(f"Interested in computer science: {'yes' if computerScience == True else 'no'}")
print(f"Interested in computer games: {'yes' if computerGames == True else 'no'}")
print(f"Have an instagram account: {'yes' if instagramAcc == True else 'no'}")