
#code for billing application 

import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("RESTAURANT BILLING SYSTEM")
root.configure(background='SeaGreen1')

Tops = Frame(root,bg='MediumPurple1',bd=20,pady=9,relief=RAISED)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('comic sans ms',35,'bold'),text='RESTAURANT BILLING SYSTEM',bd=15,bg='white smoke',
                fg='dark salmon',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='snow',bd=15,relief=SUNKEN,cursor='cross')
ReceiptCal_F.pack(side=LEFT)

Buttons_F=Frame(ReceiptCal_F,bg='gray75',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='gray75',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='gray75',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='light sky blue',bd=10,relief=RIDGE)
MenuFrame.pack(side=RIGHT)
Cost_F=Frame(MenuFrame,bg='light sky blue',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='light sky blue',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='light sky blue',bd=4,relief=RAISED)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='light sky blue',bd=4,relief=RAISED)
Food_F.pack(side=RIGHT)


###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()
ItemsDrinks = StringVar()
ItemsFoods = StringVar()

text_Input = StringVar()
operator = ""

E_Pepsi = StringVar()
E_CocaCola = StringVar()
E_DietCoke = StringVar()
E_Sprite = StringVar()
E_Fanta = StringVar()
E_MilkShakes = StringVar()
E_ColdCoffee = StringVar()
E_HotDog = StringVar()
E_VegBurger = StringVar()
E_Pasta = StringVar()
E_Sandwich = StringVar()
E_Fries = StringVar()
E_VegBiryani = StringVar()
E_Shawarma = StringVar()

E_Pepsi.set("0")
E_CocaCola.set("0")
E_DietCoke.set("0")
E_Sprite.set("0")
E_Fanta.set("0")
E_MilkShakes.set("0")
E_ColdCoffee.set("0")
E_HotDog.set("0")
E_VegBurger.set("0")
E_Pasta.set("0")
E_Sandwich.set("0")
E_Fries.set("0")
E_VegBiryani.set("0")
E_Shawarma.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno(" Exit Restaurant Billing System ","Confirm")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("0")
    SubTotal.set("0")
    TotalCost.set("0")
    CostofFood.set("0")
    CostofDrinks.set("0")
    ServiceCharge.set("0")
    ItemsDrinks.set("0")
    ItemsFoods.set("0")
    txtReceipt.delete("1.0",END)

    E_Pepsi.set("0")
    E_CocaCola.set("0")
    E_DietCoke.set("0")
    E_Sprite.set("0")
    E_Fanta.set("0")
    E_MilkShakes.set("0")
    E_ColdCoffee.set("0")
    E_HotDog.set("0")
    E_VegBurger.set("0")
    E_Pasta.set("0")
    E_Sandwich.set("0")
    E_Fries.set("0")
    E_VegBiryani.set("0")
    E_Shawarma.set("0")
    

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtPepsi.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtMilkShakes.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtHotDog.configure(state=DISABLED)
    txtVegBurger.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtFries.configure(state=DISABLED)
    txtVegBiryani.configure(state=DISABLED)
    txtShawarma.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Pepsi.get())
    Item2=float(E_CocaCola.get())
    Item3=float(E_DietCoke.get())
    Item4=float(E_Sprite.get())
    Item5=float(E_Fanta.get())
    Item6=float(E_MilkShakes.get())
    Item8=float(E_ColdCoffee.get())
    Item9=float(E_HotDog.get())
    Item10=float(E_VegBurger.get())
    Item11=float(E_Pasta.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Fries.get())
    Item15=float(E_VegBiryani.get())
    Item16=float(E_Shawarma.get())

    PriceofDrinks =(Item1 * 40) + (Item2 * 35) + (Item3 * 45) + (Item4 * 35) + (Item5 * 35) + (Item6 * 25) + (Item8 * 55)

    PriceofFood =(Item9 * 80) + (Item10 * 60) + (Item11 * 45) + (Item13 * 45) + (Item14 * 40) + (Item15 * 120) + (Item16 * 100)

    Items_Drinks = str(Item1+Item2+Item3+Item4+Item5+Item6+Item8)
    Items_Foods = str(Item9+Item10+Item11+Item13+Item14+Item15+Item16)
    
    
    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)
    
    ItemsDrinks.set(Items_Drinks)
    ItemsFoods.set(Items_Foods)

def chkPepsi():
    if(var1.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        E_Pepsi.set("")
    elif(var1.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")
        
def chk_CocaCola():
    if(var2.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var2.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_DietCoke():
    if(var3.get() == 1):
        txtDietCoke.configure(state = NORMAL)
        txtDietCoke.delete('0',END)
        txtDietCoke.focus()
    elif(var3.get() == 0):
        txtDietCoke.configure(state = DISABLED)
        E_DietCoke.set("0")
        
def chkSprite():
    if(var4.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set("")
    elif(var4.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chk_Fanta():
    if(var5.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var5.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")


def chk_MilkShakes():
    if(var6.get() == 1):
        txtMilkShakes.configure(state = NORMAL)
        txtMilkShakes.delete('0',END)
        txtMilkShakes.focus()
    elif(var6.get() == 0):
        txtMilkShakes.configure(state = DISABLED)
        E_MilkShakes.set("0")


def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chk_HotDog():
    if(var9.get() == 1):
        txtHotDog.configure(state = NORMAL)
        txtHotDog.delete('0',END)
        txtHotDog.focus()
    elif(var9.get() == 0):
        txtHotDog.configure(state = DISABLED)
        E_HotDog.set("0")

def chk_VegBurger():
    if(var10.get() == 1):
        txtVegBurger.configure(state = NORMAL)
        txtVegBurger.delete('0',END)
        txtVegBurger.focus()
    elif(var10.get() == 0):
        txtVegBurger.configure(state = DISABLED)
        E_VegBurger.set("0")


def chk_Pasta():
    if(var12.get() == 1):
        txtPasta.configure(state = NORMAL)
        txtPasta.delete('0',END)
        txtPasta.focus()
    elif(var12.get() == 0):
        txtPasta.configure(state = DISABLED)
        E_Pasta.set("0")

def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chk_Fries():
    if(var14.get() == 1):
        txtFries.configure(state = NORMAL)
        txtFries.delete('0',END)
        txtFries.focus()
    elif(var14.get() == 0):
        txtFries.configure(state = DISABLED)
        E_Fries.set("0")

def chk_VegBiryani():
    if(var15.get() == 1):
        txtVegBiryani.configure(state = NORMAL)
        txtVegBiryani.delete('0',END)
        txtVegBiryani.focus()
    elif(var15.get() == 0):
        txtVegBiryani.configure(state = DISABLED)
        E_VegBiryani.set("0")

def chk_Shawarma():
    if(var16.get() == 1):
        txtShawarma.configure(state = NORMAL)
        txtShawarma.delete('0',END)
        txtShawarma.focus()
    elif(var16.get() == 0):
        txtShawarma.configure(state = DISABLED)
        E_Shawarma.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(100199,500899)
    randomRef= str(x)
    Receipt_Ref.set("Bill No:"+ randomRef)

    
    txtReceipt.insert(END,'Receipt Ref:\t\t'+Receipt_Ref.get() +'\t\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t'+"Cost of Items \n")
    
    txtReceipt.insert(END,'Pepsi:\t\t\t\t'+ E_Pepsi.get()+'\n')
    txtReceipt.insert(END,'CocaCola:\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'DietCoke:\t\t\t\t'+ E_DietCoke.get()+'\n')
    txtReceipt.insert(END,'Sprite:\t\t\t\t' + E_Sprite.get() +'\n')
    txtReceipt.insert(END,'Fanta:\t\t\t\t'+ E_Fanta.get()+'\n')
    txtReceipt.insert(END,'MilkShakes:\t\t\t\t'+ E_MilkShakes.get()+'\n')
    txtReceipt.insert(END,'ColdCoffee:\t\t\t\t'+ E_ColdCoffee.get()+'\n')
    txtReceipt.insert(END,'HotDog:\t\t\t\t'+ E_HotDog.get()+'\n')
    txtReceipt.insert(END,'VegBurger:\t\t\t\t'+ E_VegBurger.get()+'\n')
    txtReceipt.insert(END,'Pasta:\t\t\t\t'+ E_Pasta.get()+'\n')
    txtReceipt.insert(END,'Sandwich:\t\t\t\t'+ E_Sandwich.get()+'\n')
    txtReceipt.insert(END,'Fries:\t\t\t\t'+ E_Fries.get()+'\n')
    txtReceipt.insert(END,'VegBiryani:\t\t\t\t'+ E_VegBiryani.get()+'\n')
    txtReceipt.insert(END,'Shawarma:\t\t\t\t'+ E_Shawarma.get()+'\n')
    txtReceipt.insert(END,'No. of Items(Drinks)\t\t\t\t'+ItemsDrinks.get()+"\n")
    txtReceipt.insert(END,'No. of Items(Foods)\t\t\t\t'+ItemsFoods.get()+"\n")
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t'+str(TotalCost.get())+"\n")


#########################################Drinks####################################################################

Pepsi=Checkbutton(Drinks_F,text='Pepsi(Rs.40)\t',variable=var1,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chkPepsi).grid(row=0,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='CocaCola(Rs.35)\t',variable=var2,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chk_CocaCola).grid(row=1,sticky=W)
DietCoke=Checkbutton(Drinks_F,text='DietCoke(Rs.45)\t',variable=var3,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chk_DietCoke).grid(row=2,sticky=W)
Sprite=Checkbutton(Drinks_F,text='Sprite(Rs.35)',variable=var4,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chkSprite).grid(row=3,sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta(Rs.35)',variable=var5,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chk_Fanta).grid(row=4,sticky=W)
MilkShakes=Checkbutton(Drinks_F,text='MilkShakes(Rs.25)',variable=var6,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chk_MilkShakes).grid(row=5,sticky=W)

ColdCoffee=Checkbutton(Drinks_F,text='ColdCoffee(Rs.55)',variable=var8,onvalue=1,offvalue=0,font=('courier new',18,'bold'),
                    bg='light sky blue',command=chk_ColdCoffee).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtPepsi = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=0,column=1)

txtCocaCola = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=1,column=1)

txtDietCoke = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_DietCoke)
txtDietCoke.grid(row=2,column=1)

txtSprite = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=3,column=1)

txtFanta = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=4,column=1)

txtMilkShakes= Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_MilkShakes)
txtMilkShakes.grid(row=5,column=1)

txtColdCoffee = Entry(Drinks_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED
                        ,textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7,column=1)
#############################################Foods######################################################################

HotDog = Checkbutton(Food_F,text="HotDog(Rs.80)",variable=var9,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_HotDog).grid(row=0,sticky=W)
VegBurger = Checkbutton(Food_F,text="VegBurger(Rs.60)",variable=var10,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_VegBurger).grid(row=1,sticky=W)

Pasta = Checkbutton(Food_F,text="Pasta(Rs.45) ",variable=var12,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_Pasta).grid(row=3,sticky=W)
Sandwich = Checkbutton(Food_F,text="Sandwich(Rs.45) ",variable=var13,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_Sandwich).grid(row=4,sticky=W)
Fries = Checkbutton(Food_F,text="Fries(Rs.40) ",variable=var14,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_Fries).grid(row=5,sticky=W)
VegBiryani = Checkbutton(Food_F,text="VegBiryani(Rs.120) ",variable=var15,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_VegBiryani).grid(row=6,sticky=W)
Shawarma = Checkbutton(Food_F,text="Shawarma(Rs.100) ",variable=var16,onvalue = 1, offvalue=0,
                        font=('courier new',18,'bold'),bg='light sky blue',command=chk_Shawarma).grid(row=7,sticky=W)
################################################Food Entry##########################################################
txtHotDog=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_HotDog)
txtHotDog.grid(row=0,column=1)

txtVegBurger=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_VegBurger)
txtVegBurger.grid(row=1,column=1)

txtPasta=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_Pasta)
txtPasta.grid(row=3,column=1)

txtSandwich=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtFries=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_Fries)
txtFries.grid(row=5,column=1)

txtVegBiryani=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_VegBiryani)
txtVegBiryani.grid(row=6,column=1)

txtShawarma=Entry(Food_F,font=('courier new',16,'bold'),bd=8,width=6,justify=CENTER,state=DISABLED,
                        textvariable=E_Shawarma)
txtShawarma.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblItemsDrinks=Label(Cost_F,font=('courier new',13,'bold'),text='No. of Items(Drinks):',bg='light sky blue',
                fg='black',justify=CENTER)
lblItemsDrinks.grid(row=0,column=0,sticky=W)
txtItemsDrinks=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ItemsDrinks)
txtItemsDrinks.grid(row=0,column=1)

lblCostofDrinks=Label(Cost_F,font=('courier new',13,'bold'),text='Cost of Drinks:',bg='light sky blue',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=1,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=1,column=1)

lblItemsFoods=Label(Cost_F,font=('courier new',13,'bold'),text='No. of Items(Foods):',bg='light sky blue',
                fg='black',justify=CENTER)
lblItemsFoods.grid(row=2,column=0,sticky=W)
txtItemsFoods=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ItemsFoods)
txtItemsFoods.grid(row=2,column=1)

lblCostofFood=Label(Cost_F,font=('courier new',13,'bold'),text='Cost of Foods:',bg='light sky blue',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=3,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=3,column=1)


###########################################################Payment information###################################################

lblServiceCharge=Label(Cost_F,font=('courier new',13,'bold'),text='Service Charge:',bg='light sky blue',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=0,column=2,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=0,column=3)

lblPaidTax=Label(Cost_F,font=('courier new',13,'bold'),text='Paid Tax:',bg='light sky blue',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=1,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=1,column=3)

lblSubTotal=Label(Cost_F,font=('courier new',13,'bold'),text='Sub Total:',bg='light sky blue',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=2,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=2,column=3)

lblTotalCost=Label(Cost_F,font=('courier new',13,'bold'),text='TotalCost:',bg='light sky blue',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=3,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('courier new',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=3,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=10,bg='white',bd=4,font=('courier new',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',16,'bold'),width=4,text='TOTAL',
                        bg='salmon1',command=CostofItem).grid(row=0,column=3)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',16,'bold'),width=4,text='RECEIPT',
                        bg='salmon1',command=Receipt).grid(row=0,column=2)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',16,'bold'),width=4,text='RESET',
                        bg='salmon1',command=Reset).grid(row=0,column=1)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',16,'bold'),width=4,text='EXIT',
                        bg='salmon1',command=iExit).grid(row=0,column=0)

###################################Calculator Display################################################################################


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('courier new',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='7',
                        bg='salmon1',command=lambda:btnClick(7)).grid(row=2,column=1)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='8',
                        bg='salmon1',command=lambda:btnClick(8)).grid(row=2,column=2)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='9',
                        bg='salmon1',command=lambda:btnClick(9)).grid(row=2,column=3)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='+',
                        bg='salmon1',command=lambda:btnClick('+')).grid(row=2,column=0)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='4',
                        bg='salmon1',command=lambda:btnClick(4)).grid(row=3,column=1)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='5',
                        bg='salmon1',command=lambda:btnClick(5)).grid(row=3,column=2)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='6',
                        bg='salmon1',command=lambda:btnClick(6)).grid(row=3,column=3)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='-',
                        bg='salmon1',command=lambda:btnClick('-')).grid(row=3,column=0)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='1',
                        bg='salmon1',command=lambda:btnClick(1)).grid(row=4,column=1)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='2',
                        bg='salmon1',command=lambda:btnClick(2)).grid(row=4,column=2)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='3',
                        bg='salmon1',command=lambda:btnClick(3)).grid(row=4,column=3)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='*',
                        bg='salmon1',command=lambda:btnClick('*')).grid(row=4,column=0)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='0',
                        bg='salmon1',command=lambda:btnClick(0)).grid(row=5,column=1)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='Clear',
                        bg='salmon1',command=btnClear).grid(row=5,column=2)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='=',
                        bg='salmon1',command=btnEquals).grid(row=5,column=3)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('courier new',18,'bold'),width=4,text='/',
                        bg='salmon1',command=lambda:btnClick('/')).grid(row=5,column=0)







root.mainloop()
