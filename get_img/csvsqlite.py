from __future__ import print_function
import sqlite3
import csv
import os
from pathlib import *
import glob
import sys

from csv import DictReader


conn = sqlite3.connect('..\db.sqlite3')
db = conn.cursor()
csvfilename = 'amazon.csv'
separator = ','
with open(csvfilename, 'r') as fh:
            dr = DictReader(fh, delimiter=separator)
            fieldlist=",".join(dr.fieldnames)
            ph=("?,"*len(dr.fieldnames))[:-1]
            #self.db.execute("DROP TABLE IF EXISTS %s"%tablename)
            #self.db.execute("CREATE TABLE %s(%s)"%(tablename, fieldlist))
            #ins="insert into %s (%s) values (%s)"%(tablename, fieldlist, ph)
            ins = "insert into get_img_amazon(asin,desc) values (%s)" %(ph)
            for line in dr:
                v=[]
                for k in dr.fieldnames: v.append(line[k])
                db.execute(ins, v)
conn.commit()
conn.close()


