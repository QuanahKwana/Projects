# Sorry if this is a weird thing to code about. I just don't know what else to code rn.

print("Hey, I know you've probably seen some stuff.")
talking = input("Would you like to talk about it? \n")
time_suffering = []

if talking == "yes" or talking == "sure":
    problems = input("Okay. Well, how many days have you been thinking about this kind of stuff?\n")
    for x in problems.split():
        if x.isdigit():
            time_suffering.append(int(x))
    print (str(time_suffering) + " days is quite a while to go without talking about it don't you think? \n Let's talk about it.")


else:
    print("Hey, that's fine. I understand and respect your decision.")
    exit()

sadness = input("What have you been feeling these past " + str(time_suffering) + " days?\n")
for i in sadness.split():
    if i == "sad" or i == "depressed":
        input("I am so sorry to hear about that. I am here for you.")
