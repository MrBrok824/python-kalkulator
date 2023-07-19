#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  calculator.py
#  
#  Copyright 2023 Mihajlo Bogdanović - Brok <mrmiha824@gmail.com>
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
#  script for personal needs wrote Mihajlo Bogdanović - Brok
#  web site www.paluba.info
#  script name: calculator.py
#  support, question, suggestions: <mrmiha824@gmail.com> or <brok@paluba.info>
#  Kraljevo, Serbia
#  date: 16.05.2023.

# Ova funkcija dodaje dva broja
def add(x, y):
    return x + y

# Ova funkcija oduzima dva broja
def subtract(x, y):
    return x - y

# Ova funkcija množi dva broja
def multiply(x, y):
    return x * y

# Ova funkcija deli dva broja
def divide(x, y):
    return x / y


print("Izaberite operaciju:")
print("1.Sabiranje")
print("2.Oduzmanje")
print("3.Množenje")
print("4.Deljenje")

while True:
    # uzeti unos od korisnika
    choice = input("Izaberite računsku radnju(1/2/3/4): ")

    # proverite da li je izbor jedna od četiri opcije
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Unesite prvi broj: "))
            num2 = float(input("Unesite drugi broj: "))
        except ValueError:
            print("Nepravilan unos. Molim unesite broj.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # proverite da li korisnik želi još jedan proračun
        # prekinuti while petlju ako je odgovor ne
        next_calculation = input("Hoćete li da uradimo još jednu kalkulaciju? (da/ne): ")
        if next_calculation == "ne":
          break
    else:
        print("Nepravilan unos")
