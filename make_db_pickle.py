# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:25:07 2018

@author: Oleg.Shcherbinin
"""

from initdata import db
import pickle
dbfile = open("people-pickle", "wb") # в версии 3.X следует использовать
pickle.dump(db, dbfile) # двоичный режим работы с файлами, так как
dbfile.close() # данные имеют тип bytes, а не str