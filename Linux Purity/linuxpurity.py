print("Welcome to the official Linux purity test! This seires of 20 questions will evaluate your linux purity.")
score = 100
varA = "y"
varC = "n"
varB = input("Have you used a windows version for more than a year? [y/N]")
if varC == varB:
    score = score
else:
    score = score -5

varB = input("Have you ever used a UNIX-based operating sysetm?")
if varA == varB:
    score = score
else:
    score = score -5

varB = input("Do you prefer a command-line interface (CLI) to a graphical one? (GUI)")
if varA == varB:
    score = score
else:
    score = score -5

varB = input("Do you dual-boot at least one linux distro and another OS?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Do you dual-boot linux and windows?")
if varC == varB:
    score = score
else:
    score = score -5
varB = input("Do you dual-boot two linux distros?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Do you only run linux in VMs?")
if varC == varB:
    score = score
else:
    score = score -5
varB = input("Have you ever distro-hopped?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Have you ever switched to windows from a linux distro?")
if varC == varB:
    score = score
else:
    score = score -5
varB = input("If it was up to you, would every computer in the world run some sort of UNIX?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Do you run a linux distro as your daily driver?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Have you ever used an Arch-based distro?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Have you ever used Arch?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Was your first computer running windows?")
if varC == varB:
    score = score
else:
    score = score -5
varB = input("Was your first computer running a propietary OS?")
if varC == varB:
    score = score
else:
    score = score -5
varB = input("Do you support FOSS? (Free Open-Source Software)")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Have you installed linux on a device at least 8 years old?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Do you prefer Arch to Manjaro?")
if varA == varB:
    score = score
else:
    score = score -10
varB = input("Have you ever convinced someone to try linux?")
if varA == varB:
    score = score
else:
    score = score -5
varB = input("Last question: Is Arch the best distro in the universe?")
if varA == varB:
    score = score
else:
    score = score

print("Your score is...")
print(score)
if score <= 10:
    print("Windows krill alert! Go try a linux distro and come back!")
else:
    if score <= 20 and score >= 10:
        print("Absolutely propietary! You're new, but keep trying and you will get more pure!")
    else:
        if score <= 30 and score >= 20:
            print("VM blob! You probably only run linux in VMs.")
        else:
            if score <= 40 and score >= 30:
                print("Hmm... You are working your way through various levels of purity.")
            else:
                if score <= 50 and score >= 40:
                    print("Ubuntu user! You probably are satisfied where you are and do not need to have bleeding-edge distros.")
                else:
                    if score <= 60 and score >= 50:
                        print("Arch-derived user! You probably don't want to go throught the hassle of installing Arch when you can get a near-identical distro easier. Work smarter, not harder!")
                    else:
                        if score <= 70 and score >= 60:
                            print("Average user! You probably are a total nerd =)")
                        else:
                            if score <= 80 and score >= 70:
                                print("r/foundthedebianuser! You are reasonbly advanced but like the stability of debian.")
                            else:
                                if score <= 90 and score >= 80:
                                    print("Standard Arch user. You like to go around various forums yelling 'I USE ARCH BTW!!!!'")
                                else:
                                    if score <= 95 and score >= 90:
                                        print("LinuxFromScratch. You have clearly mastered all aspects of Linux.")
                                    else:
                                        if score == 100:
                                            print("You, sir/madame, are a true god.")
