# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:45:53 2018

@author: Oleg.Shcherbinin
"""

import shelve
db = shelve.open("class-shelve")
for key in db:
    print(key, "=>\n ", db[key].name, db[key].pay)

bob = db["bob"]
print(bob.lastName())
print(db["tom"].lastName())