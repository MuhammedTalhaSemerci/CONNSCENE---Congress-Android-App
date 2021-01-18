import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk,Image
from array import *
import time
import socketio
import socket
import base64
import asyncio
import threading



i=0
sid=[]
sidupdate =[]
durdurma=0
sayi=0
b = 0
u = 0
thread_stop = 0
thread_control =0

sio = socketio.Client()

kayitarr = []
kayitarr1 = []

kayitarrsayac=0
kayitarrsayac1 = 0

sayacvar = []
sayacvarindex = 0




class SimCon :

    def sidsearch (sid,combobox):

        u = 0
        for u in range(0,len(sid),+1):

            if combobox == sid[u][1]:
            
                return u
            
            else:
                pass
            

    def kayitarr1search (sid,kayitarr1,combobox):
        m = 0
        u = 0

        
        for u in range(0,len(sid),+1):

            if combobox == sid[u][1]:

                m = u
                
            
            else:
                pass

        g = 0
        for g in range(0,len(kayitarr1),+1):
            
            if sid[m][0] == kayitarr1[g][0]:
                
                return g
            
            else:
                pass




@sio.event
def connect():
    print('Im connected!')

    
@sio.on('socket_id')
def on_message(data):

    global sid
    global i
    
    sid.insert(i,[data,data])
    
    
    
    print(sid)
    i = i+1
    
    

    
@sio.on('socket_id_delete')
def on_message(data):
    global i
    global sid
    
    
    x=0
    z = 0
    for z in range(0,len(sid),+1):
        
        print(len(sid))
        
        if z+1 <= len(sid):
            if sid[z][0]==data:
                
                x=z
                
            else:
                pass

        elif z+1 > len(sid):
            time.sleep(1)
            
            m = 0
            for m in range(0,len(sid),+1):

                    
                if m+1 <= len(sid):
                    if sid[m][0]==data:
                        
                        x=m
                        
                    else:
                        pass
            
                else:
                    break
            
                
            
    if sid[x][0] == data:
        
        sid[x][0]= ""
        sid[x][1]= "çıkış yapıldı"
        
        print(sid)
        

    else:
        pass
         
    


@sio.event    
def disconnect():
    print('bağlantı koptu')
    


def resim_ekle_guncelle():
    
    global kayitarr
   
    
    global kayitarrsayac
    
    global sid
   
    filename = filedialog.askopenfilename(title = "Select a file", filetypes = (("png files", "*.png"),("all files","*.*")))
 
    

    
    
    with open(filename, 'rb') as img_file:
        
        encodedBytes = base64.b64encode(img_file.read())
        encodedStr = str(encodedBytes, "utf-8")
        
    combobox = str(monthchoosen.get())

    u =0
    
    for u in range (0,len(sid),+1):

        if u+1 <= len(sid):

        
            if combobox == sid[u][1]:
                
                if len(kayitarr) == 0:
                    
                    kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                    
                    
                    print(filename)
                    
                    newwidth = 330
                    newheight = 350
                    image = Image.open(filename)
                    copyimage = image.copy()
                    image = copyimage.resize((newwidth,newheight))
                    
                    my_img = ImageTk.PhotoImage(image)
                    my_label.place(x=25,y=150)
                    my_label.configure(width=250,height=370)
                    
                    my_label.configure(image=my_img)
                    my_label.image = my_img
        
                    kayitarrsayac += 1
                   
                    sio.emit('kayitlidata',kayitarr)
                    
                else:
                    cakisma = 0
                    
                    
                    k = 0
                    m = 0
                    for k in range (0,len(kayitarr),+1):

                        if kayitarr[k][0]== sid[u][0]:

                            cakisma = 1
                            
                            m = k
                        else:
                            pass
                        
                    if cakisma == 1:
                        print('basarılı')
                        
                        kayitarrsayac -= 1
                        
                        
                        kayitarr.remove(kayitarr[m])
                        
                        
                        kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                        
                        
                        print(filename)
                        
                        newwidth = 330
                        newheight = 350
                        image = Image.open(filename)
                        copyimage = image.copy()
                        image = copyimage.resize((newwidth,newheight))
                        
                        my_img = ImageTk.PhotoImage(image)
                        my_label.place(x=25,y=150)
                        my_label.configure(width=250,height=370)
                        
                        my_label.configure(image=my_img)
                        my_label.image = my_img
                        
                        kayitarrsayac += 1
                      
                        sio.emit('kayitlidata',kayitarr)
        
                    else:
                        kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                        print("resim kaydedildi")
                        
                        newwidth = 330
                        newheight = 350
                        image = Image.open(filename)
                        copyimage = image.copy()
                        image = copyimage.resize((newwidth,newheight))
                        
                        my_img = ImageTk.PhotoImage(image)
                        my_label.place(x=25,y=150)
                        my_label.configure(width=250,height=370)
                        
                        my_label.configure(image=my_img)
                        my_label.image = my_img
            
                        kayitarrsayac += 1
                        
                        sio.emit('kayitlidata',kayitarr)
                    
            else:
                pass


        elif u+1 > len(sid):
            break

        
def decrease():
    
    window.destroy()
    girdi.destroy()




def durdurma():
    global kayitarrsayac
    global kayitarr
    
    global thread_stop
    
    baslatbut["state"]="active"
    combobox = str(monthchoosen.get())
    

 

    
    sio.emit('sayacdurdurma',0)
            
            
     
        
    thread_stop = 1
    
    




def update():
    
    global sid
    
    sidupdate = []
    k = 0
    
    for k in range(0,len(sid),+1):

        sidupdate.insert(k,sid[k][1])
        
    monthchoosen['values'] = (sidupdate)  


    
    


    
    
    
def show_entry_fields():
    
    baslatbut["state"] = "disabled"
    
    global sid
    global sidupdate
    global kayitarr
    global durdurma
   
    global u
    global thread_stop
    global thread_control
    
    combobox = str(monthchoosen.get())


    
    def saniyehesap():
        global thread_control
        global thread_stop
        
        thread_stop = 0
        thread_control =0
        
        value = int(hour.get())
        value1 = int(minute.get())

        
                
        sio.emit('kayit_sayac', [value,value1,0])
            
        
        
        
        
        try:
            
            temp = (value*3600 + value1*60 )

        except:
            print("Please input the right value")
        kayitsaniye = 0
        while temp >-1:

            mins,secs = divmod(temp,60) 

            hours=0
            
            if thread_stop == 1:
                
                break
            
            
            if mins >60:
               
                hours, mins = divmod(mins, 60)
                
            

            
            if kayitsaniye == 10:
                
                sio.emit('kayit_sayac', [hours,mins,secs])
                kayitsaniye = 0

            
            print(hours,":",mins,":",secs)
            time.sleep(1)
                         
            
            kayitsaniye += 1
            temp -= 1
        thread_control = 1
        thread_stop = 0
        
        
    
    kayitislem = threading.Thread(target=saniyehesap , args= ())
   
    kayitislem.start()
    
    
        
        

   
        

  

        
    value = int(hour.get())
    value1 = int(minute.get())
    kon_isim = str(name.get())
    
   
    sio.emit('kayitlitoplusayac', kayitarr1)
    sio.emit('kayitlidata', kayitarr)







#------------------------------------#

    
    

def isim_ekle():
    global sid
    global kayitarr1
    
    combobox = monthchoosen.get()
    value2 = str(name.get())
    
    sea_res_sid = SimCon.sidsearch(sid,combobox)
    sea_res_kay1= SimCon.kayitarr1search(sid,kayitarr1,combobox)
    
    if sea_res_kay1 == None :
        
        kayitarr1.insert(kayitarrsayac1,[sid[sea_res_sid][0],0,0,value2])
     
    
    else:
        kayitarr1[sea_res_kay1][3]= value2

    print(kayitarr1)
        
    
 
    
#------------------------------------#
    
    
    
    
def sureekle():
    global sid
    global kayitarr1
    
    combobox = monthchoosen.get()
    value = int(hour.get())   
    value1 = int(minute.get())
    
    sea_res_sid = SimCon.sidsearch(sid,combobox)
    sea_res_kay1= SimCon.kayitarr1search(sid,kayitarr1,combobox)
    
    if sea_res_kay1 == None :
        
        kayitarr1.insert(kayitarrsayac1,[sid[sea_res_sid][0],value,value1,''])
     
    
    else:
        kayitarr1[sea_res_kay1][1]= value
        kayitarr1[sea_res_kay1][2]= value1
        
    print(kayitarr1)
        
    
 
    
#------------------------------------#
    
                
def guncelle():
    global sid
    global kayitarr
    global kayitarr1
    
    sio.emit('kayitlidata',kayitarr)
    sio.emit('kayitlitoplusayac',kayitarr1)
        
    
 
    
#------------------------------------#                
                       
                    
                    
                
                
def on_exit():
     if messagebox.askyesno("Exit", "Uygulamadan çıkmak istediğinize emin misiniz?"):
         window.destroy()
         girdi.destroy()
        
    
def hepsiniekle():
    
    global kayitarr
    global kayitarr1
    
    global kayitarrsayac
    global kayitarrsayac1
    global sid
    
    
    value = int(hour.get())
    value1 = int(minute.get())
    kon_isim = str(name.get())
    combobox = monthchoosen.get()

    filename = filedialog.askopenfilename(title = "Select a file", filetypes = (("png files", "*.png"),("all files","*.*")))
    
    print(kayitarr1)
    with open(filename, 'rb') as img_file:
        
        encodedBytes = base64.b64encode(img_file.read())
        encodedStr = str(encodedBytes, "utf-8")
        
    
    
    u =0
    
    for u in range (0,len(sid),+1):

        if u+1 <= len(sid):
            
            if combobox == sid[u][1]:
                print("başarılı")
                if len(kayitarr) == 0 or len(kayitarr1) == 0:
                    
                    if len(kayitarr) == 0:
                        
                        kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                        
                        
                        print(filename)
                        
                        newwidth = 330
                        newheight = 350
                        image = Image.open(filename)
                        copyimage = image.copy()
                        image = copyimage.resize((newwidth,newheight))
                        
                        my_img = ImageTk.PhotoImage(image)
                        my_label.place(x=25,y=150)
                        my_label.configure(width=250,height=370)
                        
                        my_label.configure(image=my_img)
                        my_label.image = my_img
            
                        kayitarrsayac += 1
                       
                        sio.emit('kayitlidata',kayitarr)

                    if len(kayitarr1) == 0:
                        
                        
                        kayitarr1.insert(kayitarrsayac1,[sid[u][0],value,value1,kon_isim])
                        print(filename)

                        kayitarrsayac1 += 1
                        sio.emit('kayitlidata',kayitarr)
                    
                    
                else:
                    cakisma = 0
                    cakisma1= 0
                    print("elseçalıştı")
                    
                    k = 0
                    m = 0
                    for k in range (0,len(kayitarr),+1):

                        if kayitarr[k][0]== sid[u][0]:

                            cakisma = 1
                            
                            
                            m = k
                            
                        else:
                            pass
                        
                    z = 0
                    l = 0
                    
                    for z in range (0,len(kayitarr1),+1):

                        if kayitarr1[z][0]== sid[u][0]:

                            cakisma1 = 1
                            
                            l = z
                        else:
                            pass
                    print(cakisma)
                    print(cakisma1)
                    
                    if cakisma == 1:
                        print('basarılı')
                        
                        kayitarrsayac -= 1
                        
                        
                        kayitarr.remove(kayitarr[m])
                        
                        
                        kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                        
                        
                        print(filename)
                        
                        newwidth = 330
                        newheight = 350
                        image = Image.open(filename)
                        copyimage = image.copy()
                        image = copyimage.resize((newwidth,newheight))
                        
                        my_img = ImageTk.PhotoImage(image)
                        my_label.place(x=25,y=150)
                        my_label.configure(width=250,height=370)
                        
                        my_label.configure(image=my_img)
                        my_label.image = my_img
                        
                        kayitarrsayac += 1
                      
                        sio.emit('kayitlidata',kayitarr)

                    else:
                        print("resim kaydedildi")
                        kayitarr.insert(kayitarrsayac,[sid[u][0],encodedStr])
                       
                        
                        newwidth = 330
                        newheight = 350
                        image = Image.open(filename)
                        copyimage = image.copy()
                        image = copyimage.resize((newwidth,newheight))
                        
                        my_img = ImageTk.PhotoImage(image)
                        my_label.place(x=25,y=150)
                        my_label.configure(width=250,height=370)
                        
                        my_label.configure(image=my_img)
                        my_label.image = my_img
            
                        kayitarrsayac += 1
                       
                        sio.emit('kayitlidata',kayitarr)

                        
                    if cakisma1 == 1:
                        
                        kayitarrsayac1 -= 1
                        
                        kayitarr1.remove(kayitarr1[l])
                        
                        kayitarr1.insert(kayitarrsayac1,[sid[u][0],value,value1,kon_isim])
     
                        kayitarrsayac1 += 1
                        

                       
                    else:

                        kayitarr1.insert(kayitarrsayac1,[sid[u][0],value,value1,kon_isim])
                        
  
                        kayitarrsayac1 += 1
                    print(cakisma)
                        
            
            else:
                pass

        elif u+1 > len(sidupdate):
            
            break

def sayacekle():
    global sid
    global sayacvarindex
    global sayacvar

    combobox = monthchoosen.get()
    
    u = 0
    k = 0
    cakisma = 0
        
    
    for u in range (0,len(sid),+1):
        
        if combobox == sid[u][1]:

            
            for k in range(0,len(sayacvar),+1):
                if sid[u][0] == sayacvar[k][0]:
                    
                    sayacvar[k][1]= 1
                    cakisma = 1
                    
        
                

                else:
                    pass
    if cakisma == 1:
        sio.emit('sayacvar',sayacvar)
        
    if cakisma == 0:
        i = 0
        for i in range(0,len(sid),+1):
            if combobox == sid[i][1]:
                
                sayacvar.insert(sayacvarindex,[sid[i][0],1])
                sayacvarindex += 1
                sio.emit('sayacvar',sayacvar)


def sayaccikar():
    global sid
    global sayacvarindex
    global sayacvar

    combobox = monthchoosen.get()
    
    u = 0
    k = 0
    for u in range (u,len(sid),+1):
        if combobox == sid[u][1]:

            k = u
        else :
            pass

    h = 0
    cakisma = 0
    for h in range (h,len(sayacvar),+1):
        if sayacvar[h][0] == sid[k][0]:
            sayacvar[h][1] = 0
            
            sio.emit('sayacvar',sayacvar)
            cakisma = 1

        else:
            pass
        
    if cakisma == 0 :
        
        sayacvar.insert(sayacvarindex,[sid[u][0],0])
        sayacvarindex += 1
        sio.emit('sayacvar',sayacvar)
        

def ıd_olustur():
    global b
    global sid
    global kayitarr
    global kayitarr1
    global kayitarrsayac
    global kayitarrsayac1
    global sayacvar
    
    value = int(hour.get())   
    value1 = int(minute.get())
    value2 = str(name.get())
    combobox = monthchoosen.get()

    sidupdate = []
    alinacakdeger = 0
    b = 0
   
    u = 0
    for u in range (u,len(sid),+1):

        if u+1 <= len(sid):
        
            if combobox == sid[u][1]:
                alinacakdeger = sid[u][0]
            else:
                pass
        elif u+1 > len(sid):
            break
    
    
    if len(kayitarr1) < len(sid):

        sio.emit('sayacdurdurma',0)

        m = 0
        cakisma = 0
        for m in range(0,len(kayitarr1),+1):
            
            if kayitarr1[m][0] == alinacakdeger:
                kayitarr1[m][1]=value
                kayitarr1[m][2]=value1
                kayitarr1[m][3]=value2
                cakisma = 1
                print("eski veri")
                print(kayitarr1[m])
                sio.emit('kayitlitoplusayac', [kayitarr1[m]])
                

            else:
                pass

        if cakisma == 0 :
            kayitarr1.insert(kayitarrsayac1,[alinacakdeger,value,value1,value2])
           
            kayitarrsayac1 += 1
            print("yeni ekleme")
            
            print(kayitarrsayac1-1)
            print(kayitarr1[kayitarrsayac1-1])
            kayitarr2 = kayitarr1[kayitarrsayac1-1]
            sio.emit('kayitlitoplusayac', [kayitarr1[kayitarrsayac1-1]])
                
        else:
            pass


    elif len(kayitarr1) >= len(sid):

        

        m = 0
        cakisma = 0
        for m in range(0,len(kayitarr1),+1):
            
            if kayitarr1[m][0] == alinacakdeger:
                kayitarr1[m][1]=value
                kayitarr1[m][2]=value1
                kayitarr1[m][3]=value2
                cakisma = 1
                
                sio.emit('kayitlitoplusayac', kayitarr1)
                

            else:
                pass

        if cakisma == 0 :
            kayitarr1.insert(kayitarrsayac,[alinacakdeger,value,value1,value2])
            
            kayitarrsayac1 += 1
            sio.emit('kayitlitoplusayac', kayitarr1)
                
        else:
            pass

    

    
    def updatecombo():
        global b
        global sid

        sidupdate = []
        
        combobox = monthchoosen.get()
        
        if b+1 <= len(sid):
                
            newcomboname=textinput.get()

            i = 0
            h = 0
            for i in range(0,len(sid),+1):
               
                if combobox == sid[i][1]:
                    
                    h = i
                else:
                    pass
                    
            print(sid)
            sid[h][1] = newcomboname


            i = 0
            h = 0
            for i in range(0,len(sid),+1):
                
                sidupdate.insert(i,sid[i][1])
                
            
                    
            monthchoosen['values'] = (sidupdate)
            print(sidupdate)
            
            updatescrn.destroy()
            
        elif b+1 >len(sid):
            
            updatescrn.destroy()

    if combobox != "":
        
        b = 0
        x = 0
        for b in range (0,len(sid),+1):

            if b+1 <= len(sid):
            
                if sid[b][0] == combobox:
                    
                    x = 1
                        

                else:
                    pass
            elif b+1 > len(sid):
                break

            
        if x == 1:

            updatescrn=tk.Tk()
            updatescrn.geometry("100x70")



                
            textinput = tk.Entry(updatescrn)
            textinput.grid(row=1, column=1,columnspan=1)

            
            
            update= tk.Button(master=updatescrn, text="update", command=updatecombo)
            update.grid(row=3, column=1, sticky="nsew")
            updatescrn.attributes('-topmost', True)
            updatescrn.mainloop()

        else:
            pass






def secimislemleri():

    combobox = methodchoose.get()

    if combobox == 'İsim ekle':
        isim_ekle()

    if combobox == 'Süre ekle':
        sureekle()
    
    if combobox == 'Resim güncelle':

        resim_ekle_guncelle()

        
    if combobox == 'Hepsini ekle':

        hepsiniekle()
        
    if combobox == 'Güncelle':

        guncelle()

    if combobox == 'ID Oluştur':

        ıd_olustur()









sio.connect('http://'+socket.gethostbyname(socket.gethostname())+':3000')
    

    
window = Tk()
window.geometry("300x600")
window.title("Time Counter") 
window.resizable(False, False)
window.overrideredirect(True)

girdi = tk.Tk()


girdi.protocol("WM_DELETE_WINDOW", on_exit)




  

  
# Combobox creation 
tk1 = tk.StringVar() 
monthchoosen = ttk.Combobox(girdi, width = 40, textvariable = tk1) 
  
# Adding combobox drop down list 
monthchoosen['values'] = ('') 
  
monthchoosen.grid(column = 5, row = 1) 
monthchoosen.current() 
#--------------------------------------------------#

tk2 = tk.StringVar() 
methodchoose = ttk.Combobox(window, width = 25 ,textvariable = tk2) 
  
# Adding combobox drop down list 
methodchoose['values'] = ('ID Oluştur','İsim ekle','Süre ekle','Hepsini ekle','Resim güncelle','Güncelle') 
  
methodchoose.grid(column = 3, row = 7) 
methodchoose.current() 




window.rowconfigure([0,1,2], minsize=5, weight=1)
window.columnconfigure([0, 1, 2 , 3 , 4 , 5 , 6 ,7], minsize=10, weight=10)



hour=StringVar() 
minute=StringVar() 
second=StringVar()
name = StringVar()
   
# setting the default value as 0 
hour.set("00") 
minute.set("00") 
second.set("00") 
name.set("")   
# Use of Entry class to take input from the user 
hourEntry= Entry(window, width=3, font=("Arial",18,""), 
                 textvariable=hour) 
hourEntry.grid(padx=20 , pady=20)
hourEntry.place(x=80,y=50 ) 

   
minuteEntry= Entry(window, width=3, font=("Arial",18,""), 
                   textvariable=minute) 
minuteEntry.grid(padx=20 , pady=20)
minuteEntry.place(x=130,y=50 ) 



   
secondEntry= Entry(window, width=3, font=("Arial",18,""), 
                   textvariable=second) 
secondEntry.grid(padx=20 , pady=20)
secondEntry.place(x=180,y=50)



nameEntry= Entry(window, width=11, font=("Arial",18,""), textvariable=name) 
nameEntry.grid(padx=20 , pady=20)
nameEntry.place(x=80,y=100)


my_label = Label(window,text ="image", image="",)
my_label.place(x=-150,y=150)


#-------------------------------#


secim = tk.Button(master=window, text="Onayla", command=secimislemleri)
secim.grid(row=10, column=3, sticky="nsew")

#-------------------------------#


sayacvarmı= tk.Button(master=window, text="sayaç ekle", command=sayacekle)
sayacvarmı.grid(row=0, column=5, sticky="nsew")
sayacvarmı.place(x=80,y=10)


sayacvarmı1= tk.Button(master=window, text="sayaç çıkar", command=sayaccikar)
sayacvarmı1.grid(row=0, column=6, sticky="nsew")
sayacvarmı1.place(x=150,y=10)

girdi.rowconfigure([0,1,2], minsize=5, weight=1)
girdi.columnconfigure([0, 1, 2 , 3 , 4 , 5 , 6 ,7], minsize=10, weight=10)


baslatbut = tk.Button(girdi, text='Başlat', command=show_entry_fields)
baslatbut.grid(row=1, column=6, sticky=tk.W, pady=4)

durdurbut = tk.Button(girdi, text='Durdur', command=durdurma)
durdurbut.grid(row=1, column=7, sticky=tk.W, pady=4)

btn_decrease = tk.Button(master=girdi, text="Quit", command=decrease)
btn_decrease.grid(row=1, column=0, sticky="nsew")



updatebtn= tk.Button(master=girdi, text="Update list", command=update)
updatebtn.grid(row=1, column=4, sticky="nsew")

window.lift()
girdi.lift()

window.attributes('-topmost', True)
#girdi.attributes('-topmost', True)


window.mainloop()
girdi.mainloop()


