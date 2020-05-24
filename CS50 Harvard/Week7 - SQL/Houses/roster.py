from cs50 import SQL
import csv
import sys

db = SQL("sqlite:///students.db")

try:
    house = sys.argv[1]
except:
    print("Usage: python roster.py 'House name'")
    exit(1)

query = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house) 

for row in query:
    
    first = row['first']
    middle = row['middle']
    last = row['last']
    birth = row['birth']
    
    if middle != None:
        
        print(f"{first} {middle} {last}, born {birth}")
    
    else:
        print(f"{first} {last}, born {birth}")

