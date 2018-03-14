# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:39:54 2018

@author: Oleg.Shcherbinin
"""

from initdata import bob, sue
import shelve
db = shelve.open("people-shelve")
db["bob"] = bob
db["sue"] = sue
db.close()