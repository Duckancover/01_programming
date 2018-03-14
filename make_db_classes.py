# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:44:44 2018

@author: Oleg.Shcherbinin
"""

import shelve
from person import Person
from manager import Manager
bob = Person("Bob Smith", 42, 30000, "software")
sue = Person("Sue Jones", 45, 40000, "hardware")
tom = Manager("Tom Doe", 50, 50000)
db = shelve.open("class-shelve")
db["bob"] = bob
db["sue"] = sue
db["tom"] = tom
db.close()