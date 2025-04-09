from guizero import App, Text, TextBox, PushButton
def fetch_response():
    user = submits.value
    if user == "1234":
        sleep(1)
        app.hide()

def Keypad__1():
   submits.append('1')
def Keypad__2():
   submits.append('2')
def Keypad__3():
   submits.append('3')
def Keypad__4():
   submits.append('4')
def Keypad__5():
   submits.append('5')
def Keypad__6():
   submits.append('6')
def Keypad__7():
   submits.append('7')
def Keypad__8():
   submits.append('8')
def Keypad__9():
   submits.append('9')
def Keypad__0():
   submits.append('0')
def Clearapp():
   submits.clear()
submit = PushButton(app, fetch_response, text="Submit", grid=[410, 300])
Clear_app = PushButton(app, Clearapp, text="Clear", grid=[410, 325])
app = App(title="KeyPad", width=800, height=480, layout="grid")
Keypad_1 = PushButton(App, Keypad__1, text="1", grid=[0, 400])
Keypad_1.width = 8
Keypad_1.height = 4
Keypad_2 = PushButton(app, Keypad__2, text="2", grid=[50, 400])
Keypad_2.width = 8
Keypad_2.height = 4
Keypad_3 = PushButton(app, Keypad__3, text="3", grid=[100, 400])
Keypad_3.width = 8
Keypad_3.height = 4
Keypad_4 = PushButton(app, Keypad__4, text="4", grid=[0, 450])
Keypad_4.width = 8
Keypad_4.height = 4
Keypad_5 = PushButton(app, Keypad__5, text="5", grid=[50, 450])
Keypad_5.width = 8
Keypad_5.height = 4
Keypad_6 = PushButton(app, Keypad__6, text="6", grid=[100, 450])
Keypad_6.width = 8
Keypad_6.height = 4
Keypad_7 = PushButton(app, Keypad__7, text="7", grid=[0, 500])
Keypad_7.width = 8
Keypad_7.height = 4
Keypad_8 = PushButton(app, Keypad__8, text="8", grid=[50, 500])
Keypad_8.width = 8
