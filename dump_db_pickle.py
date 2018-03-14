# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:26:54 2018

@author: Oleg.Shcherbinin
"""

import pickle
dbfile = open("people-pickle", "rb") # в версии 3.X следует использовать
db = pickle.load(dbfile) # двоичный режим работы с файлами
for key in db:
    print(key, "=>\n ", db[key])
print(db["sue"]["name"])