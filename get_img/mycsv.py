from __future__ import print_function
import sqlite3
import csv
import os
from pathlib import *
import glob
import sys

import sqlite3
from csv import DictReader

class SQLiteDB():
    #def __init__(self, dbname=':memory:'):
    #    self.db=sqlite3.connect(dbname)

    def importFromCSV(self, csvfilename, tablename, separator=",",dbname="db.sqlite3"):
        conn = sqlite3.connect('..\db.sqlite3')
        db = conn.cursor()
        with open(csvfilename, 'r') as fh:
            dr = DictReader(fh, delimiter=separator)
            fieldlist=",".join(dr.fieldnames)
            ph=("?,"*len(dr.fieldnames))[:-1]
            self.db.execute("DROP TABLE IF EXISTS %s"%tablename)
            self.db.execute("CREATE TABLE %s(%s)"%(tablename, fieldlist))
            ins="insert into %s (%s) values (%s)"%(tablename, fieldlist, ph)
            for line in dr:
                v=[]
                for k in dr.fieldnames: v.append(line[k])
                self.db.execute(ins, v)
        self.db.commit()

if __name__ == '__main__':
    #db=SQLiteDB("mydatabase.sqlite")
    #db.importFromCSV("mydata.csv", "mytable")
    #db=SQLiteDB('..\db.sqlite3')
    SQLiteDB.importFromCSV("amazon.csv", "get_img_amazon","..\db.sqlite3")
