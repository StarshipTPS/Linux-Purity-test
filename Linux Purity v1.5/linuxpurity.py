print("Welcome to the official Linux purity test! This seires of 20 questions will evaluate your linux purity.")
score = 100
yes = "y"
no = "n"
player = input("Have you used a windows version for more than a year? [y/N]")
if no == player:
    score = score
else:
    score = score -5

player = input("Have you ever used a UNIX-based operating sysetm?")
if yes == player:
    score = score
else:
    score = score -5

player = input("Do you prefer a command-line interface (CLI) to a graphical one? (GUI)")
if yes == player:
    score = score
else:
    score = score -5

player = input("Do you dual-boot at least one linux distro and another OS?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Do you dual-boot linux and windows?")
if no == player:
    score = score
else:
    score = score -5
player = input("Do you enjoy using linux?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Do you only run linux in VMs?")
if no == player:
    score = score
else:
    score = score -5
player = input("Have you ever distro-hopped?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Have you ever switched to windows from a linux distro?")
if no == player:
    score = score
else:
    score = score -5
player = input("If it was up to you, would every computer in the world run some sort of UNIX?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Do you run a linux distro as your daily driver?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Do you use the default desktop instead of customizing it?")
if no == player:
    score = score
else:
    score = score -5
player = input("Do you know any programming languages")
if yes == player:
    score = score
else:
    score = score -5
player = input("Have you ever created your own linux distro?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Was your first computer running a propietary OS?")
if no == player:
    score = score
else:
    score = score -5
player = input("Do you use FOSS? (Free Open-Source Software)")
if yes == player:
    score = score
else:
    score = score -5
player = input("Have you installed linux on a device at least 8 years old?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Do you prefer GNOME to another DE (Desktop environment)?")
if no == player:
    score = score
else:
    score = score -10
player = input("Have you ever convinced someone to try linux?")
if yes == player:
    score = score
else:
    score = score -5
player = input("Last question: Is Arch the best distro in the universe?")

print("Your score is...")
print(score)
if score <= 10:
    print("Windows krill alert! Go try a linux distro and come back!")
elif score <= 20 and score >= 10:
    print("Absolutely propietary! You're new, but keep trying and you will get more pure!")
elif score <= 30 and score >= 20:
    print("VM blob! You probably only run linux in VMs.")
elif score <= 40 and score >= 30:
    print("Hmm... You are working your way through various levels of purity.")
elif score <= 50 and score >= 40:
    print("You probably use windows only because work/school reqquires you to.")
elif score <= 60 and score >= 50:
    print("You are a linux user that probably doesn't distrohop and lives on one distro.")
elif score <= 70 and score >= 60:
    print("Average user! You probably are a total nerd =)")
elif score <= 80 and score >= 70:
    print("You are one of the top purity levels. You are a credit to the linux community.")
elif score <= 90 and score >= 80:
    print("Standard Arch user. You like to go around various forums yelling 'I USE ARCH BTW!!!!'")
elif score <= 95 and score >= 90:
    print("LinuxFromScratch. You have clearly mastered all aspects of Linux.")
elif score == 100:
    print("You, sir/madame, are a true god.")
