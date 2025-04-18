import tkinter as tk

calcuation=""

def add(symbol):
    global calcuation
    calcuation+=str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calcuation)

def evaluate():
    global calcuation
    try:
        calcuation=str(eval(calcuation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calcuation)
    except:
        clear()
        text_result.insert(1.0,'Error')



def clear():
    global calcuation
    calcuation=""
    text_result.delete(1.0,'end')


root=tk.Tk()
root.title("shafiul's calculator")
root.geometry('300x275')
text_result=tk.Text(root,height=2,width=16,font=("arial",24))
text_result.grid(columnspan=5)

btn1=tk.Button(root,text='1',command=lambda:add(1),width=5,font=('arial',14))
btn1.grid(row=2,column=1)
btn2=tk.Button(root,text='2',command=lambda:add(2),width=5,font=('arial',14))
btn2.grid(row=2,column=2)
btn3=tk.Button(root,text='3',command=lambda:add(3),width=5,font=('arial',14))
btn3.grid(row=2,column=3)
btn4=tk.Button(root,text='4',command=lambda:add(4),width=5,font=('arial',14))
btn4.grid(row=3,column=1)
btn5=tk.Button(root,text='5',command=lambda:add(5),width=5,font=('arial',14))
btn5.grid(row=3,column=2)
btn6=tk.Button(root,text='6',command=lambda:add(6),width=5,font=('arial',14))
btn6.grid(row=3,column=3)
btn7=tk.Button(root,text='7',command=lambda:add(7),width=5,font=('arial',14))
btn7.grid(row=4,column=1)
btn8=tk.Button(root,text='8',command=lambda:add(8),width=5,font=('arial',14))
btn8.grid(row=4,column=2)
btn9=tk.Button(root,text='9',command=lambda:add(9),width=5,font=('arial',14))
btn9.grid(row=4,column=3)
btn0=tk.Button(root,text='0',command=lambda:add(0),width=5,font=('arial',14))
btn0.grid(row=5,column=2)
btnp=tk.Button(root,text='+',command=lambda:add('+'),width=5,font=('arial',14))
btnp.grid(row=2,column=4)
btns=tk.Button(root,text='-',command=lambda:add("-"),width=5,font=('arial',14))
btns.grid(row=3,column=4)
btnm=tk.Button(root,text='x',command=lambda:add('*'),width=5,font=('arial',14))
btnm.grid(row=4,column=4)
btnd=tk.Button(root,text='/',command=lambda:add('/'),width=5,font=('arial',14))
btnd.grid(row=5,column=4)
btne=tk.Button(root,text='=',command=evaluate,width=11,font=('arial',14))
btne.grid(row=6,column=1,columnspan=2)
btno=tk.Button(root,text='(',command=lambda:add('('),width=5,font=('arial',14))
btno.grid(row=5,column=1)
btnc=tk.Button(root,text=')',command=lambda:add(')'),width=5,font=('arial',14))
btnc.grid(row=5,column=3)
btncl=tk.Button(root,text='AC',command=clear,width=11,font=('arial',14))
btncl.grid(row=6,column=3,columnspan=2)

root.mainloop()