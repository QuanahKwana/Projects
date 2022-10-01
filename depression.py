import PySimpleGUI as sg

# I know this doesn't work right now, I'm committing to github to save progress and paste it into my big computer
# Sorry if this is a weird thing to code about. I just don't know what else to code rn.

# Layout of the window
starting_question = [[sg.Text("Hey, I know you've probably seen some stuff.")],
                     [sg.Text("Would you like to talk about it?")],
                     [sg.Button("Sure", key="-sure-")],
                     [sg.Button("No", key="-no-")],
                     [sg.Text(size=(69, 1), key='-output-')],
                     [sg.Button(key='-ok-')]
                     ]

# Making Window
window = sg.Window('Sad App', starting_question)

# Calling Window
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "-sure-":
        window['-output-'].update("Oh okay! Let's talk about it.")
        window['-ok-'].update("OK!")
    if event == "-no-":
        break
window.close()

# if talking == "yes" or talking == "sure":
#    problems = input("Okay. Well, how many days have you been thinking about this kind of stuff?\n")
#    for x in problems.split():
#        if x.isdigit():
#            time_suffering.append(int(x))
#    print (str(time_suffering) + " days is quite a while to go without talking about it, don't you think? \n
#    Let's talk about it.")

# else:
#    print("Hey, that's fine. I understand and respect your decision.")
#    exit()

# sadness = input("What have you been feeling these past " + str(time_suffering) + " days?\n")
# for i in sadness.split():
#    if i == "sad" or i == "depressed":
#        input("I am so sorry to hear about that. I am here for you.")
