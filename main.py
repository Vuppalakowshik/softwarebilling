from tkinter import *
#functionality part
def total():
    #cosmetics price calculation
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
    grocerytax = totalgroceryprice * 0.18
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f'{grocerytax} Rs')
    #grocerypricecalculationends here

    #Cold drink calculation starts here

    Maazaprice=int(MaazaEntry.get())*10
    Pepsiprice=int(pepsiEntry.get())*12
    spriteprice=int(spriteEntry.get())*15
    dewprice=int(dewEntry.get())*15
    cococolaprice=int(cococolaEntry.get())*15

    totalcolddrinkprice=Maazaprice+Pepsiprice+spriteprice+dewprice+cococolaprice

    drinkspriceEntry.delete(0,END)
    colddrinktax= totalcolddrinkprice * 0.12
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f'{colddrinktax} Rs')
    drinkspriceEntry.insert(0,f'{totalcolddrinkprice} Rs')








#GUIPRT

root=Tk()
root.title('Reatail billing system')
root.geometry('1270x685')
root.iconbitmap('billingicon.ico')
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

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7 ,width=10)
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
                   ,bd=5,width=8,pady=10)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='E-mail',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
emailButton.grid(row=0,column=3,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
printButton.grid(row=0,column=4,pady=20,padx=5)


clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
clearButton.grid(row=0,column=5,pady=20,padx=5)




root.mainloop()