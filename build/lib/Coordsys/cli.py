#! /usr/bin/python3

import click
import numpy as np
from Tkinter import *


@click.command()
def main():
    """ CoordSys :: Conv is  a GUI application for conversion between the various coordinate systems.

        Steps involved in conversion :

        1) Enter the values of known coordinates separated by ','

        2) Click Calculate to obtain the necessary coordinates. """

    root = Tk()

#Modifying GUI
    root.title("CoordSys :: Converter")
    root.configure(bg="peach puff")

#Variables
    var_1 = StringVar()
    var_2 = StringVar()
    var_3 = StringVar()
    var_4 = StringVar()
    var_5 = StringVar()
    var_6 = StringVar()

    #Main Head
    label_head = Label(root,text="Coordinate System Conversions",font=("Times",20),foreground="saddle brown",bg="peach puff")
    label_head.place(x=520,y=40)

    #Button actions and respective funtions
    def cart_to_cy():
        label_cart_cy = Label(root,text="x,y and z :",bd=0,bg="thistle")
        label_cart_cy.place(x=180,y=210)
        entry_x = Entry(root,textvariable=var_1)
        entry_x.place(x=250,y=210)
        def calc():
            x=float(var_1.get().split(',')[0])
            y=float(var_1.get().split(',')[1])
            z=float(var_1.get().split(',')[2])
            rho = (x**2+y**2)**0.5
            theta = np.arctan(y/x)
            label_new_coor = Label(root,text="rho,theta and z:",bd=0,bg="thistle")
            label_new_coor.place(x=180,y=250)
            label_result = Label(root,text=(str("%.3f"%rho)+", "+str("%.3f"%theta)+" and "+str("%.3f"%z)),bd=0,bg="khaki")
            label_result.place(x=300,y=250)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",bg="light blue",bd=0,highlightbackground="black")
        button_calc.place(x=210,y=300)

    def cart_to_sp():
        label_cart_sp = Label(root,text="x,y and z :",bd=0,bg="thistle")
        label_cart_sp.place(x=560,y=210)
        entry_x = Entry(root,textvariable=var_2)
        entry_x.place(x=670,y=210)
        def calc():
            x=float(var_2.get().split(',')[0])
            y=float(var_2.get().split(',')[1])
            z=float(var_2.get().split(',')[2])
            r = (x**2+y**2+z**2)**0.5
            phi = np.arccos(z/r)
            theta = np.arcsin(y/(r*(np.sin(phi))))
            label_new_coor = Label(root,text="r,phi and theta:",bd=0,bg="thistle")
            label_new_coor.place(x=560,y=250)
            label_result = Label(root,text=(str("%.3f"%r)+", "+str("%.3f"%phi)+" and "+str("%.3f"%theta)),bd=0,bg="khaki")
            label_result.place(x=670,y=250)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",bg="light blue",bd=0,highlightbackground="black")
        button_calc.place(x=640,y=300)
        
    def cy_to_cart():
        label_cy_cart = Label(root,text="rho,theta and z :",bd=0,bg="thistle")
        label_cy_cart.place(x=1000,y=210)
        entry_x = Entry(root,textvariable=var_3)
        entry_x.place(x=1120,y=210)
        def calc():
            rho=float(var_3.get().split(',')[0])
            theta=float(var_3.get().split(',')[1])
            z=float(var_3.get().split(',')[2])
            x = rho*np.cos(theta)
            y = rho*np.sin(theta)
            label_new_coor = Label(root,text="x, y and z : ",bd=0,bg="thistle")
            label_new_coor.place(x=1000,y=250)
            label_result = Label(root,text=(str("%.3f"%x)+", "+str("%.3f"%y)+" and "+str("%.3f"%z)),bd=0,bg="khaki")
            label_result.place(x=1120,y=250)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",bg="light blue",bd=0,highlightbackground="black")
        button_calc.place(x=1080,y=300)

    def sp_to_cart():
        label_sp_cart = Label(root,text="r,phi and theta :",bd=0,bg="thistle")
        label_sp_cart.place(x=180,y=480)
        entry_x = Entry(root,textvariable=var_4)
        entry_x.place(x=300,y=480)
        def calc():
            r=float(var_4.get().split(',')[0])
            phi=float(var_4.get().split(',')[1])
            theta=float(var_4.get().split(',')[2])
            x  = r*np.sin(phi)*np.cos(theta)
            y = r*np.sin(phi)*np.sin(theta)
            z = r * np.cos(phi)
            label_new_coor = Label(root,text="x,y and z:",bd=0,bg="thistle")
            label_new_coor.place(x=180,y=520)
            label_result = Label(root,text=(str("%.3f"%x)+", "+str("%.3f"%y)+" and "+str("%.3f"%z)),bd=0,bg="khaki")
            label_result.place(x=300,y=520)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",bg="light blue",bd=0,highlightbackground="black")
        button_calc.place(x=210,y=560)

    def cy_to_sp():
        label_cy_sp = Label(root,text="rho,theta and z :",bd=0,bg="thistle")
        label_cy_sp.place(x=560,y=480)
        entry_x = Entry(root,textvariable=var_5)
        entry_x.place(x=700,y=480)
        def calc():
            rho=float(var_5.get().split(',')[0])
            theta=float(var_5.get().split(',')[1])
            z=float(var_5.get().split(',')[2])
            r = (rho**2+z**2)**0.5
            phi = np.arccos(z/r)
            label_new_coor = Label(root,text="r,phi and theta:",bd=0,bg="thistle")
            label_new_coor.place(x=560,y=520)
            label_result = Label(root,text=(str("%.3f"%r)+", "+str("%.3f"%phi)+" and "+str("%.3f"%theta)),bd=0,bg="khaki")
            label_result.place(x=700,y=520)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",bg="light blue",bd=0,highlightbackground="black")
        button_calc.place(x=640,y=560)

    def sp_to_cy():
        label_sp_cy = Label(root,text="r,phi and theta :",bd=0,bg="thistle")
        label_sp_cy.place(x=1010,y=480)
        entry_x = Entry(root,textvariable=var_6)
        entry_x.place(x=1130,y=480)
        def calc():
            r=float(var_6.get().split(',')[0])
            phi=float(var_6.get().split(',')[1])
            theta=float(var_6.get().split(',')[2])
            rho =  r * np.sin(phi)
            z = r * np.cos(phi)
            label_new_coor = Label(root,text="rho,theta and z:",bd=0,bg="thistle")
            label_new_coor.place(x=1010,y=520)
            label_result = Label(root,text=(str("%.3f"%rho)+", "+str("%.3f"%theta)+" and "+str("%.3f"%z)),bd=0,bg="khaki")
            label_result.place(x=1130,y=520)
        button_calc = Button(root,text="Calculate",command=calc,activebackground="olive drab",activeforeground="gray69",cursor="hand1",highlightbackground="black",bd=0,bg="light blue")
        button_calc.place(x=1080,y=560)



    #Buttons
    button_cart_cy = Button(root,text="Cartesian to Cylindrical",command=cart_to_cy,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_cart_cy.place(x=180,y=150)
    button_cart_sp = Button(root,text="Cartesian to Spherical",command=cart_to_sp,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_cart_sp.place(x=600,y=150)
    button_cy_cart = Button(root,text="Cylindrical to Cartesian",command=cy_to_cart,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_cy_cart.place(x=1030,y=150)
    button_sp_cart = Button(root,text="Spherical to Cartesian",command=sp_to_cart,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_sp_cart.place(x=180,y=420)
    button_cy_sp = Button(root,text="Cylindrical to Spherical",command=cy_to_sp,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_cy_sp.place(x=600,y=420)
    button_sp_cy = Button(root,text="Spherical to Cylindrical",command=sp_to_cy,activebackground="light yellow",activeforeground="red",cursor="hand1",bg="light pink",bd=0)
    button_sp_cy.place(x=1030,y=420)

    #Fun
    cr = Label(root,text="Copyright 2018 Amogh.A.Joshi. All rights reserved.",relief=SUNKEN,cursor="gumby")
    cr.pack(side=BOTTOM,fill=X)

    #Mainloop
    root.mainloop()

if __name__ == "__main__":
    main()
