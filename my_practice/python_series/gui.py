import tkinter

def thanks():
    print('thanks..')

window = tkinter.Tk()
window.title('Sign In')
window.geometry('250x150')

label = tkinter.Label(window, text= 'First Name').grid(row=0,column=0)

f1=tkinter.Entry(window).grid(row=0,column=1)

label1 = tkinter.Label(window, text= 'Last Name').grid(row=1,column=0)

f2=tkinter.Entry(window).grid(row=1,column=1)

label2 = tkinter.Label(window, text= 'password').grid(row=2,column=0)

f3=tkinter.Entry(window).grid(row=2,column=1)

label3 = tkinter.Label(window, text= 'confirm password').grid(row=3,column=0)

f1=tkinter.Entry(window).grid(row=3,column=1)

button = tkinter.Button(window,text='SUBMIT',fg='green',bg='powderblue',command=thanks).grid()
button1 = tkinter.Button(window,text = 'CANCEL',fg='red',bg='powderblue',command=quit).grid(row=4,column=1)



window.mainloop()


