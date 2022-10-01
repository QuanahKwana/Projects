import PySimpleGUI as sg

# I know this doesn't work right now, I'm committing to gitHub to save progress and paste it into my big computer
# Sorry if this is a weird thing to code about. I just don't know what else to code rn.

# Layout of the window
starting_question = [[sg.Text("Hey, I know you've probably seen some stuff.\nWould you like to talk about it?", background_color="lavender", text_color="black")],
                     [sg.Button("Sure", key="-sure-")],
                     [sg.Button("No", key="-no-")],
                     [sg.Text(size=(69, 1), key='-output-', visible=False, background_color="lavender", text_color="black")],
                     [sg.Button(key='-ok-', visible=False,)]
                     ]

paragraph = [[sg.Text('Please write down how you feel')],
             [sg.Multiline(size=(100, 500))]
             ]

image = [[sg.Image(source="legosi.png")]]

vent = [
    [
        sg.Column(paragraph),
        sg.VerticalSeparator(pad=(50, 50)),
        sg.Column(image)
        ]
]
# Making Window
window = sg.Window('Sad App', starting_question, background_color="lavender")

# Calling Window
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "-sure-":
        window['-output-'].update("Oh okay! Let's talk about it.", visible=True)
        window['-ok-'].update("OK!", visible=True)
    if event == "-no-":
        break
    if event == '-ok-':
        window.close()
        window = sg.Window('Helping', vent, size=(1920, 1080))
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
