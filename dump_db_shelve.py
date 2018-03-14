# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:41:34 2018

@author: Oleg.Shcherbinin
"""

import shelve
db = shelve.open("people-shelve")
for key in db:
    print(key, "=>\n ", db[key])
print(db["sue"]["name"])
db.close()