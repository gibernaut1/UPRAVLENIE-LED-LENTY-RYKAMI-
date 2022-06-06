from tkinter import *
import pyautogui
import webbrowser

tk = Tk()
tk.geometry('850x650')


def privat():
    webbrowser.open('https://privatbank.ua/')
    pyautogui.moveTo(1100, 250, duration=5)
    pyautogui.PAUSE = 3
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1100, 520, duration=3)
    pyautogui.click()
    pyautogui.PAUSE = 5
    pyautogui.typewrite('672594571')
    pyautogui.moveTo(1180, 520, duration=3)
    pyautogui.click()
    pyautogui.moveTo(710, 580, duration=5)
    pyautogui.click()


def ukrsibbank():
    webbrowser.open('https://my.ukrsibbank.com/ru/personal/')
    pyautogui.moveTo(1220, 180, duration=5)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.moveTo(1130,470,duration=3)
    pyautogui.PAUSE = 3
    pyautogui.click()
    pyautogui.typewrite('672594571')
    pyautogui.PAUSE = 5
    pyautogui.moveTo(1130, 510,duration=3)
    #pyautogui.scroll(-800)
    # pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.typewrite('sobaka12')
    # pyautogui.PAUSE = 5
    # pyautogui.keyDown('Enter')
    pyautogui.moveTo(1130, 600)
    pyautogui.keyDown('Enter')
    pyautogui.click()


def idea():
    webbrowser.open(
        'https://ideabank.ua/uk')
    pyautogui.moveTo(1200, 200, duration=7)
    pyautogui.click()
    pyautogui.moveTo(1200, 240, duration=1)
    pyautogui.click()
    pyautogui.moveTo(550, 505, duration=5)
    pyautogui.click()


def privatNatasha():
    webbrowser.open('https://privatbank.ua/')
    pyautogui.moveTo(1100, 250, duration=2)
    pyautogui.PAUSE = 1
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.moveTo(1100, 520, duration=1)
    pyautogui.click()
    pyautogui.PAUSE = 1
    pyautogui.typewrite('687775632')
    pyautogui.moveTo(1180, 520, duration=1)
    pyautogui.click()
    pyautogui.moveTo(710, 570, duration=5)
    pyautogui.click()




def alfa():
    webbrowser.open('https://my.alfabank.com.ua')
    # pyautogui.moveTo(1470,300,duration=5)
    # pyautogui.click()
    # pyautogui.moveTo(1470,350,duration=1)
    # pyautogui.click()
    pyautogui.moveTo(700, 300, duration=5)
    pyautogui.click()
    pyautogui.PAUSE = 2
    pyautogui.typewrite('0')
    pyautogui.typewrite('672594571')
    pyautogui.PAUSE = 1
    pyautogui.moveTo(700, 420, duration=5)
    pyautogui.click()
    pyautogui.typewrite('12.04.1962')
    pyautogui.moveTo(700, 510, duration=5)
    pyautogui.click()
    pyautogui.moveTo(710, 400, duration=5)
    pyautogui.click()
    pyautogui.moveTo(720, 450, duration=5)
    pyautogui.click()


def oschad():
    webbrowser.open('https://online.oschadbank.ua/wb/')
    # pyautogui.moveTo(1470,300,duration=5)
    # pyautogui.click()
    # pyautogui.moveTo(1470,350,duration=1)
    # pyautogui.click()
    pyautogui.moveTo(750, 410, duration=5)
    pyautogui.click()
    pyautogui.moveTo(750, 400, duration=5)
    pyautogui.click()
    pyautogui.moveTo(650, 450, duration=5)
    pyautogui.click()
    pyautogui.moveTo(650, 500, duration=5)
    pyautogui.click()


def prozorroMAN():
    webbrowser.open('https://prozorro.gov.ua/')
    # pyautogui.moveTo(1470,300,duration=5)
    # pyautogui.click()
    # pyautogui.moveTo(1470,350,duration=1)
    # pyautogui.click()
    pyautogui.moveTo(750, 410, duration=8)
    pyautogui.click()
    pyautogui.typewrite('32827468')
    pyautogui.PAUSE = 1

    pyautogui.click()
    pyautogui.PAUSE = 4
    pyautogui.moveTo(1200,400,duration=8)
    pyautogui.click()

    # pyautogui.keyDown('Enter')
    pyautogui.PAUSE = 2
    pyautogui.scroll(-800, )


lb1 = Label(text='Банки', bg="red", fg="yellow").place(x=45, y=10)
btn1 = Button(bg='yellow', text="Приватбанк", command=privat, width=15).place(x=5, y=35)
btn2 = Button(bg='lightblue', text="Укрсиббанк", command=ukrsibbank, width=15).place(x=5, y=85)
btn3 = Button(bg='lightgreen', text="Idea", command=idea, width=15).place(x=5, y=135)
btn4 = Button(bg='beige', text="Наталья", command=privatNatasha, width=15).place(x=5, y=185)
btn5 = Button(bg='gold', text="Альфа", command=alfa, width=15).place(x=5, y=235)
btn6 = Button(bg='orange', text="Ощадбанк", command=oschad, width=15).place(x=5, y=285)
lb2 = Label(text='Прозорро', bg='red', fg="yellow").place(x=35, y=335)
btn7 = Button(text='МАН', bg='violet', command=prozorroMAN, fg='yellow', width=15).place(x=5, y=365)
#tk.mainloop()
