import tkinter
import threading
import time

root = tkinter.Tk()
root.title("水果机")
root.minsize(300,300)

btn1 = tkinter.Button(root,text="桃子",bg="red")
btn1.place(x=20,y=20,width=50,height=50)

btn2 = tkinter.Button(root,text="西瓜",bg="white")
btn2.place(x=90,y=20,width=50,height=50)

btn3 = tkinter.Button(root,text="苹果",bg="white")
btn3.place(x=160,y=20,width=50,height=50)

btn4 = tkinter.Button(root,text="香蕉",bg="white")
btn4.place(x=230,y=20,width=50,height=50)

btn5 = tkinter.Button(root,text="草莓",bg="white")
btn5.place(x=230,y=90,width=50,height=50)

btn6 = tkinter.Button(root,text="菠萝",bg="white")
btn6.place(x=230,y=160,width=50,height=50)

btn7 = tkinter.Button(root,text="花生",bg="white")
btn7.place(x=230,y=230,width=50,height=50)

btn8 = tkinter.Button(root,text="柿子",bg="white")
btn8.place(x=160,y=230,width=50,height=50)

btn9 = tkinter.Button(root,text="葡萄",bg="white")
btn9.place(x=90,y=230,width=50,height=50)

btn10 = tkinter.Button(root,text="橙子",bg="white")
btn10.place(x=20,y=230,width=50,height=50)

btn11 = tkinter.Button(root,text="荔枝",bg="white")
btn11.place(x=20,y=160,width=50,height=50)

btn12 = tkinter.Button(root,text="核桃",bg="white")
btn12.place(x=20,y=90,width=50,height=50)

fruitlist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]

isloop = False
stopsgin = False
stopid = None

def rund():
    global isloop
    global stopid

    if isloop == True:
        return
    i = 1
    if isinstance(stopid,int):
        i = stopid

    while True:
        time.sleep(0.01)
        for x in fruitlist:
            x["bg"] = "pink"

        fruitlist[i]["bg"] = "green"
        i += 1
        print("当前i",i)

        if i >= len(fruitlist):
            i = 0

        if stopsign == True:
            isloop = False
            stopid = i
            break

def newtask():
    global isloop
    global stopsign

    stopsign = False
    t = threading.Thread(target=rund)
    t.start()
    isloop = True

def stop():
    global stopsign

    # time.sleep(1)
    if stopsign == True:
        return
    stopsign = True



btn_start = tkinter.Button(root,text="开始",bg="white",command=newtask)
btn_start.place(x=90,y=125,width=50,height=50)

btn_stop = tkinter.Button(root,text="停止",bg="white",command=stop)
btn_stop.place(x=160,y=125,width=50,height=50)

root.mainloop()