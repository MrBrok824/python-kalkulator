#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sites_link_search_engine.py
#  
#  Copyright 2023 Mihajlo Bogdanović <mrmiha824@gmail.com>
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
#  #  script for personal needs wrote Mihajlo Bogdanović Brok
#  for learning Python programming language
#  web site www.paluba.info
#  script name: sites_link_search_engine.py
#  suggestions and questions: <mrmiha824@gmail.com> or <brok@paluba.info>
#  Kraljevo, Serbia, Europe
#  date: 16.05.2023.

  
import requests
import re

# unesi url
url = input('Unesi URL domena (uključujući obavezno i `http://`): ')

# povežite se sa URL-om
website = requests.get(url)

# čitaj html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# izlaz linova
for link in links:
    print (link[0])

