from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib,sys
#functionality part
def clear():
    RiceEntry.delete(0,END)
    daalEntry.delete(0,END)
    oilEntry.delete(0,END)
    WheatEntry.delete(0,END)
    SugarEntry.delete(0,END)
    TeaEntry.delete(0,END)
    #fancyitems
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    #drinksprice
    pepsiEntry.delete(0,END)
    cococolaEntry.delete(0,END)
    MaazaEntry.delete(0,END)
    spriteEntry.delete(0,END)
    frootiEntry.delete(0,END)
    dewEntry.delete(0,END)
#INSERTION TAKE S PLACE

    RiceEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    WheatEntry.insert(0, 0)
    SugarEntry.insert(0, 0)
    TeaEntry.insert(0, 0)
    # fancyitems
    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    # drinksprice
    pepsiEntry.insert(0, 0)
    cococolaEntry.insert(0, 0)
    MaazaEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    dewEntry.insert(0,0)
#END INSERTION
    cosmetictaxEntry.delete(0,END) #taxentry
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)
    #pricentry
    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('success', 'bill is successfully send',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong pease try again')


    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('err0r', 'bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send-email')
        root.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)


        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text='RECIPINENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverLabel = Label(recipientFrame, text="Email-Adress", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(senderFrame, text="message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=20, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()






def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('err0r','bill is empty')
    else:
        file=tempfile.mkdtemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')





def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')





if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result =  messagebox.askyesno('Confirm','DO you want to save the bill?')
    if  result:
       bill_content=textarea.get(1.0,END)
       file=open(f'bills/{billnumber}.txt','w')
       file.write(bill_content)
       file.close()
       messagebox.showinfo('Success',f' {billnumber} is saved successfully' )
       billnumber = random.randint(500,1000)

billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()==''or phoneEntry=='':
        messagebox.showerror('Error','cusomer detail Are  required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()== '' and  drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()== '0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No products are selected')
    else:
        textarea.delete(1.0 ,END)
        textarea.insert(END,'\t\t**WELCOME Customer**')
        textarea.insert(END,f'\n Bill Number: {billnumber}')
        textarea.insert(END, f'\n Customer name: {nameEntry.get()}')
        textarea.insert(END, f'\n Phone number: {phoneEntry.get()}')
        textarea.insert(END,'\n =====================================================\n')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n =====================================================\n')
        if int(bathsoapEntry.get()) > 0:
            textarea.insert(END, f'Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}\n')
        if int(facecreamEntry.get()) > 0:
            textarea.insert(END, f'Face cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}\n')
        if int(facewashEntry.get()) > 0:
            textarea.insert(END, f'Face wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice}\n')
        if int(hairgelEntry.get()) > 0:
            textarea.insert(END, f'Hair gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice}\n')
        if int(hairsprayEntry.get()) > 0:
            textarea.insert(END, f'Hair spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice}\n')
        if int(bodylotionEntry.get()) > 0:
            textarea.insert(END, f'Body lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice}\n')
        if int(RiceEntry.get()) > 0:
            textarea.insert(END, f'Rice\t\t\t{RiceEntry.get()}\t\t\t{riceprice}\n')
        if int(oilEntry.get()) > 0:
            textarea.insert(END, f'Oil\t\t\t{oilEntry.get()}\t\t\t{oilprice}\n')
        if int(daalEntry.get()) > 0:
            textarea.insert(END, f'Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice}\n')
        if int(WheatEntry.get()) > 0:
            textarea.insert(END, f'Wheat\t\t\t{WheatEntry.get()}\t\t\t{Wheatprice}\n')
        if int(SugarEntry.get()) > 0:
            textarea.insert(END, f'Sugar\t\t\t{SugarEntry.get()}\t\t\t{sugarprice}\n')
        if int(TeaEntry.get()) > 0:
            textarea.insert(END, f'Tea\t\t\t{TeaEntry.get()}\t\t\t{teaprice}\n')
        if int(MaazaEntry.get()) > 0:
            textarea.insert(END, f'Maaza\t\t\t{MaazaEntry.get()}\t\t\t{Maazaprice}\n')
        if int(pepsiEntry.get()) > 0:
            textarea.insert(END, f'Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{Pepsiprice}\n')
        if int(dewEntry.get()) > 0:
            textarea.insert(END, f'Dew\t\t\t{dewEntry.get()}\t\t\t{dewprice}\n')
        if int(frootiEntry.get()) > 0:
            textarea.insert(END, f'Frooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice}\n')
        if int(cococolaEntry.get()) > 0:
            textarea.insert(END, f'Cococola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice}\n')
        if int(spriteEntry.get()) > 0:
            textarea.insert(END, f'Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice}\n')

    textarea.insert(END, '\n =====================================================\n')
    if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax \t\t\t {cosmetictaxEntry.get()}\n')
    if grocerytaxEntry.get()!= '0.0 Rs':
        textarea.insert(END, f'Grocery Tax \t\t {grocerytaxEntry.get()}\n')
    if drinkstaxEntry.get()!= '0.0 Rs':()

    textarea.insert(END, f' drink Tax\t\t {drinkstaxEntry.get()}\n')

    textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}')
    textarea.insert(END, '\n =====================================================\n')
    save_bill()







def total():
    #cosmetics price calculation
    global soapprice,facecreamprice,facewashprice,hairgelprice,hairsprayprice,bodylotionprice
    global riceprice,oilprice,daalprice,Wheatprice,sugarprice,teaprice
    global Maazaprice, Pepsiprice, dewprice, frootiprice, cococolaprice,spriteprice
    global totalbill
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairgelprice = int(hairgelEntry.get())*150
    hairsprayprice = int(hairsprayEntry.get())*80
    bodylotionprice = int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Rs')
    #cosmetics caluculation ends here

    #Grocery calculation starts here
    riceprice=int(RiceEntry.get())*200
    oilprice=int(oilEntry.get())*150
    daalprice = int(daalEntry.get()) * 100
    Wheatprice = int(WheatEntry.get()) * 200
    sugarprice = int(SugarEntry.get()) *120
    teaprice = int(TeaEntry.get()) * 120

    totalgroceryprice=riceprice+oilprice+daalprice+Wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax = totalgroceryprice * 0.5
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f'{grocerytax} Rs')
    #grocerypricecalculationends here

    #Cold drink calculation starts here

    Maazaprice=int(MaazaEntry.get())*10
    Pepsiprice=int(pepsiEntry.get())*12
    spriteprice=int(spriteEntry.get())*15
    dewprice=int(dewEntry.get())*15
    frootiprice=int(frootiEntry.get())*15
    cococolaprice=int(cococolaEntry.get())*15

    totalcolddrinkprice=Maazaprice+Pepsiprice+spriteprice+dewprice+cococolaprice+frootiprice

    drinkspriceEntry.delete(0,END)
    colddrinktax= totalcolddrinkprice * 0.12
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f'{colddrinktax} Rs')
    drinkspriceEntry.insert(0,f'{totalcolddrinkprice} Rs')

    totalbill=totalcosmeticprice+totalcolddrinkprice+totalgroceryprice+cosmetictax+grocerytax+colddrinktax




#GUIPRT

root=Tk()
root.title('Reatail billing system')
root.geometry('1270x685')

# handle icon setting cleanly
if getattr(sys, 'frozen', False):
    # Running in a bundle (like exe), skip setting icon
    pass
else:
    # Running from .py file
    root.iconbitmap('billingicon.ico')
import os
app_icon = os.path.join(os.path.dirname(__file__), 'billingicon.ico')
root.iconbitmap(app_icon)
headingLabel=Label(root,text='Reatail Billing System',font=('times new roman',30,'bold')
,bg='gray20',fg='gold', bd=12,relief=GROOVE)
headingLabel.pack(fill=X)
customer_details_frame=LabelFrame(root,text='Customer details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')

customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20'
                ,fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7 ,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)


productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticFrame=LabelFrame(productsFrame,text='Cosmotics' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticFrame,text='bathsoap',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
bathsoapLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticFrame,text='Facecream',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
facecreamLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticFrame,text='Facewash',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
facewashLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticFrame,text='Hairspray',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
hairsprayLabel.grid(row=3,column=0 ,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)


hairgelLabel=Label(cosmeticFrame,text='Hairgel',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
hairgelLabel.grid(row=4,column=0 ,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticFrame,text='bodylotion',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
bodylotionLabel.grid(row=5,column=0 ,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticFrame, font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

RiceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
RiceLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
RiceEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=9,padx=10)
RiceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='OIL',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
oilLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
daalLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

WheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
WheatLabel.grid(row=3,column=0 ,pady=9,padx=10,sticky='w')
WheatEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
WheatEntry.grid(row=3,column=1,pady=9,padx=10)
WheatEntry.insert(0,0)

SugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
SugarLabel.grid(row=4,column=0 ,pady=9,padx=10,sticky='w')
SugarEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
SugarEntry.grid(row=4,column=1,pady=9,padx=10)
SugarEntry.insert(0,0)


TeaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
TeaLabel.grid(row=5,column=0 ,pady=9,padx=10,sticky='w')
TeaEntry=Entry(groceryFrame, font=('times new roman',15,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)




drinksFrame=LabelFrame(productsFrame,text='Cold drinks' ,font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

MaazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
MaazaLabel.grid(row=0,column=0 ,pady=9,padx=10,sticky='w')
MaazaEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
MaazaEntry.grid(row=0,column=1,pady=9,padx=10)
MaazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
pepsiLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
spriteLabel.grid(row=2,column=0 ,pady=9,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
dewLabel.grid(row=3,column=0 ,pady=9,padx=10,sticky='w')
dewEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)


frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
frootiLabel.grid(row=4,column=0 ,pady=9,padx=10,sticky='w')
frootiEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text=' Cococola',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
cococolaLabel.grid(row=5,column=0 ,pady=9,padx=10,sticky='w')
cococolaEntry=Entry(drinksFrame, font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)
billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',13,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=20,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


billmenuFrame=LabelFrame(root,text='Billmenu' ,font=('times new roman',13,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack(padx=5,fill=X)

cosmeticpriceLabel=Label(billmenuFrame,text=' Cosmoticprice',font=('times new roman',10,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
cosmeticpriceLabel.grid(row=0,column=0 ,pady=5,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame, font=('times new roman',10,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel=Label(billmenuFrame,text=' Groceryprice',font=('times new roman',10,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
grocerypriceLabel.grid(row=1,column=0 ,pady=9,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame, font=('times new roman',10,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)


drinkspriceLabel = Label(billmenuFrame, text=' Cold Drinks Price', font=('times new roman',10,'bold'),
                         fg='white', bd=5, relief=GROOVE, bg='gray20')
drinkspriceLabel.grid(row=2, column=0, pady=2, padx=5, sticky='w')

drinkspriceEntry = Entry(billmenuFrame, font=('times new roman',10,'bold'), width=10, bd=4)
drinkspriceEntry.grid(row=2, column=1, pady=2, padx=5)



cosmetictaxLabel=Label(billmenuFrame,text=' Cosmotictax',font=('times new roman',10,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
cosmetictaxLabel.grid(row=0,column=2,pady=5,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame, font=('times new roman',10,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel=Label(billmenuFrame,text=' Grocerytax',font=('times new roman',10,'bold'),
                                  fg='white',bd=8,relief=GROOVE,bg='gray20')
grocerytaxLabel.grid(row=1,column=2 ,pady=9,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame, font=('times new roman',10,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)


drinkstaxLabel = Label(billmenuFrame, text=' Cold Drinks tax', font=('times new roman',10,'bold'),
                         fg='white', bd=5, relief=GROOVE, bg='gray20')
drinkstaxLabel.grid(row=2, column=2, pady=2, padx=5, sticky='w')

drinkstaxEntry = Entry(billmenuFrame, font=('times new roman',10,'bold'), width=10, bd=4)
drinkstaxEntry.grid(row=2, column=3, pady=2, padx=5)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='E-mail',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10 ,command=send_email)
emailButton.grid(row=0,column=3,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=4,pady=20,padx=5)


clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=5,pady=20,padx=5)




root.mainloop()