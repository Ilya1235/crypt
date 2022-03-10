import urllib.request, base64, PIL, urllib, tkinter
from tkinter import *
from PIL import ImageTk
from urllib import *

raw_data = urllib.request.urlopen("https://clck.ru/dYsMj").read()

b64_data = base64.b64encode(raw_data)

class App:
    def __init__(self):
        self.window = Tk()
        self.image = PhotoImage(data = b64_data)
        self.window.title("Шифровальщик (alpha build v0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1)")
        self.window.call('wm', 'iconphoto', self.window._w, self.image)

        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.message_1 = StringVar()
        self.message_2 = StringVar()
        self.message_3 = StringVar()
        self.crypt_sel = StringVar()
        self.mode_sele = StringVar()
        self.final_res = StringVar()

        self.mode_sele.set("Режим")
        self.crypt_sel.set("Шифр")
        self.message_1.set("Выражение")
        self.message_2.set("Шаг")
        self.message_3.set("Кодовое слово")
        self.final_res.set("Результат")

        self.window.dropd_1 = OptionMenu(self.window, self.mode_sele, *["Шифрование", "Дешифрование"]).grid(row = 1, column = 0)
        self.window.dropd_2 = OptionMenu(self.window, self.crypt_sel, *["Шифр Цезаря", "Цифр Цезаря с кодовым словом"]).grid(row = 1, column = 1)

        self.window.entry_1 = Entry(self.window, textvariable = self.message_1).grid(row = 1, column = 2)
        self.window.entry_2 = Entry(self.window, textvariable = self.message_2).grid(row = 1, column = 3)
        self.window.entry_3 = Entry(self.window, textvariable = self.message_3).grid(row = 1, column = 4)
        self.window.entry_4 = Entry(self.window, textvariable = self.final_res).grid(row = 2, column = 0)

        self.window.buttn_1 = Button(self.window, text = "Ввод", command = self.butt_act).grid(row = 1, column = 5)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def butt_act(self):
        if self.mode_sele.get() == "Шифрование": 
            if self.crypt_sel.get() == "Шифр Цезаря":
                self.final_res.set(caesar(self.message_1.get(), int(self.message_2.get())))
            elif self.crypt_sel.get() == "Цифр Цезаря с кодовым словом":
                self.final_res.set(caesar_word(self.message_1.get(), int(self.message_2.get()), self.message_3.get()))
        else:
            if self.crypt_sel.get() == "Шифр Цезаря":
                self.final_res.set(caesar(self.message_1.get(), -1 * int(self.message_2.get())))
            elif self.crypt_sel.get() == "Цифр Цезаря с кодовым словом":
                self.final_res.set(caesar_word(self.message_1.get(), -1 * int(self.message_2.get()), self.message_3.get()))

def caesar(string, step):
    alp_ru = [i for i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?-() "']
    alp_en = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;:!?-()" ']
    string = [i for i in string]
    if string[0] in alp_ru:
        for i in range(len(string)):
            string[i] = alp_ru[(alp_ru.index(string[i]) + step) % len(alp_ru)]
    elif string[0] in alp_en:
        for i in range(len(string)):
            string[i] = alp_en[(alp_en.index(string[i]) + step) % len(alp_en)]
    return ''.join(string)

def caesar_word(string, step, key_word):
    answer_f = ''
    alp_ru_b = list(map(lambda x: x.upper(), [i for i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,;:!?-() "']))
    alp_ru_s = list(map(lambda x: x.lower(), [k for k in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?-() "']))
    alp_en_b = list(map(lambda x: x.upper(), [j for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,;:!?-()" ']))
    alp_en_s = list(map(lambda x: x.lower(), [f for f in 'abcdefghijklmnopqrstuvwxyz.,;:!?-()" ']))
    key_word = [l for l in key_word]
    if key_word[0] in alp_en_b or key_word[0] in alp_en_s:
        for i in range(len(key_word)):
            ch_key_s = key_word[i].lower()
            ch_key_b = key_word[i].upper()
            if ch_key_s in alp_en_s:
                alp_en_s.remove(ch_key_s)
                alp_en_b.remove(ch_key_b)
        alp_en_s = list(map(lambda x: x.lower(), key_word)) + alp_en_s
        alp_en_b = list(map(lambda x: x.upper(), key_word)) + alp_en_b
    elif key_word[0] in alp_ru_b or key_word[0] in alp_ru_s:
        for i in range(len(key_word)):
            ch_key_s = key_word[i].lower()
            ch_key_b = key_word[i].upper()
            if ch_key_s in alp_ru_s:
                alp_ru_s.remove(ch_key_s)
                alp_ru_b.remove(ch_key_b)
        alp_ru_s = list(map(lambda x: x.lower(), key_word)) + alp_ru_s
        alp_ru_b = list(map(lambda x: x.upper(), key_word)) + alp_ru_b

    for i in range(len(string)):
        if string[i] in alp_en_b:
            answer_f += alp_en_b[(alp_en_b.index(string[i]) + step) % len(alp_en_b)]
        elif string[i] in alp_en_s:
            answer_f += alp_en_s[(alp_en_s.index(string[i]) + step) % len(alp_en_s)]
        elif string[i] in alp_ru_s:
            answer_f += alp_ru_s[(alp_ru_s.index(string[i]) + step) % len(alp_ru_s)]
        elif string[i] in alp_ru_b:
            answer_f += alp_ru_b[(alp_ru_b.index(string[i]) + step) % len(alp_ru_b)]
    
    return answer_f

app = App()  