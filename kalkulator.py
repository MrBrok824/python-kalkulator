#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  običan kalulator.py
#  
#  Copyright 2024 MrBrok <mrmiha824@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# MrBrok for Brok-Hak-Lab
# kontakt <mrmiha824@gmail.com>
# 02.02.2024. Serbia


import tkinter as tk

root = tk.Tk()  # Prozor glavnog menija
root.title("Običan kalulator͏͏")
e = tk.Entry(root,
             width=35,
             bg='#f0ffff',
             fg='black',
             borderwidth=5,
             justify='right',
             font='Calibri 15')
e.grid(row=0, column=0, columnspan=3, padx=12, pady=12)


def buttonClick(num):  # Funkcija za klikove
    temp = e.get(
    )  # Privremena promenljiva za čuvanje trenutnog unosa na ekranu
    e.delete(0, tk.END)
    e.insert(0, temp + num)  # Ubacivanje ulaznog broja


def buttonClear():  # Funkcija za čišćenje
    e.delete(0, tk.END)


def buttonGet(
        oper
):  # Funkcija za čuvanje prvog unosa i štampanje '+, -, /, *'
    global num1, math  # Globalna promenljiva num1 i matematika za upotrebu u funkciji buttonEkual()
    num1 = e.get()  # Dobijanje prvog broja
    math = oper
    e.insert(tk.END, math)
    try:
        num1 = float(num1)
    except ValueError:
        buttonClear()


def buttonEqual():
    inp = e.get()
    num2 = float(inp[inp.index(math) + 1:])  # Dobijanje drugog broja
    e.delete(0, tk.END)
    if math == '+':  # Sabiranje
        e.insert(0, str(num1 + num2))
    elif math == '-':  # Oduzimanje
        e.insert(0, str(num1 - num2))
    elif math == 'x':  # Množenje
        e.insert(0, str(num1 * num2))
    elif math == '/':  # Deljenje
        try:
            e.insert(0, str(num1 / num2))
        except ZeroDivisionError:
            # U slučaju da u imeniocu postoji nula, odgovor je nedefinisan
            e.insert(0, 'Undefined')


# Definisanje dugmića:
b1 = tk.Button(root,
               text='1',
               padx=40,
               pady=10,
               command=lambda: buttonClick('1'),
               font='Calibri 12')
b2 = tk.Button(root,
               text='2',
               padx=40,
               pady=10,
               command=lambda: buttonClick('2'),
               font='Calibri 12')
b3 = tk.Button(root,
               text='3',
               padx=40,
               pady=10,
               command=lambda: buttonClick('3'),
               font='Calibri 12')
b4 = tk.Button(root,
               text='4',
               padx=40,
               pady=10,
               command=lambda: buttonClick('4'),
               font='Calibri 12')
b5 = tk.Button(root,
               text='5',
               padx=40,
               pady=10,
               command=lambda: buttonClick('5'),
               font='Calibri 12')
b6 = tk.Button(root,
               text='6',
               padx=40,
               pady=10,
               command=lambda: buttonClick('6'),
               font='Calibri 12')
b7 = tk.Button(root,
               text='7',
               padx=40,
               pady=10,
               command=lambda: buttonClick('7'),
               font='Calibri 12')
b8 = tk.Button(root,
               text='8',
               padx=40,
               pady=10,
               command=lambda: buttonClick('8'),
               font='Calibri 12')
b9 = tk.Button(root,
               text='9',
               padx=40,
               pady=10,
               command=lambda: buttonClick('9'),
               font='Calibri 12')
b0 = tk.Button(root,
               text='0',
               padx=40,
               pady=10,
               command=lambda: buttonClick('0'),
               font='Calibri 12')
bdot = tk.Button(root,
                 text='.',
                 padx=41,
                 pady=10,
                 command=lambda: buttonClick('.'),
                 font='Calibri 12')

badd = tk.Button(root,
                 text='+',
                 padx=29,
                 pady=10,
                 command=lambda: buttonGet('+'),
                 font='Calibri 12')
bsub = tk.Button(root,
                 text='-',
                 padx=30,
                 pady=10,
                 command=lambda: buttonGet('-'),
                 font='Calibri 12')
bmul = tk.Button(root,
                 text='x',
                 padx=30,
                 pady=10,
                 command=lambda: buttonGet('x'),
                 font='Calibri 12')
bdiv = tk.Button(root,
                 text='/',
                 padx=30.5,
                 pady=10,
                 command=lambda: buttonGet('/'),
                 font='Calibri 12')

bclear = tk.Button(root,
                   text='PONIŠTI SVE',
                   padx=20,
                   pady=10,
                   command=buttonClear,
                   font='Calibri 12')
bequal = tk.Button(root,
                   text='=',
                   padx=39,
                   pady=10,
                   command=buttonEqual,
                   font='Calibri 12')

# Postavljanje dugmića na ekran u redove i kolone:
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
badd.grid(row=3, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bmul.grid(row=2, column=3)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bdiv.grid(row=1, column=3)

b0.grid(row=4, column=0)
bdot.grid(row=4, column=1)
bequal.grid(row=4, column=2)
bsub.grid(row=4, column=3)

bclear.grid(row=0, column=3)

# Otvaranje prozora:
root.mainloop()
