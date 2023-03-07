import wget
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title('启动器下载器')
window.geometry('180x100')
window.resizable(0, 0)


def startDownload(*args):
    if cbox.get() == 'PCL2':
        target = 'PCL2.exe'
        dl = wget.download(url='http://mirror.yaka.fun/api/PCL.exe', out=target)
        messagebox.showinfo(title='Info', message='下载完毕')
    elif cbox.get() == 'HMCL':
        target = 'HMCL.exe'
        # 不要问这个URL为什么没有.exe的后缀，问就是我改文件名的时候忘了加exe
        dl = wget.download(url='http://mirror.yaka.fun/api/HMCL', out=target)
        messagebox.showinfo(title='Info', message='下载完毕')
    elif cbox.get() == 'BakaXL':
        target = 'BakaXL.exe'
        dl = wget.download(url='http://mirror.yaka.fun/api/BakaXL.exe', out=target)
        messagebox.showinfo(title='Info', message='下载完毕')


cbox = ttk.Combobox(window, width=20)
cbox.place(x=10, y=10)
cbox['values'] = ['PCL2', 'HMCL', 'BakaXL']
cbox.current(0)
cbox['state'] = 'readonly'
btn = tk.Button(window, text='下载', width=22, height=2, bd=1, command=startDownload)
btn.place(x=10, y=40)
window.mainloop()
