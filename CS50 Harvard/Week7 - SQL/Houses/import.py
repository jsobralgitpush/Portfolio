from cs50 import SQL
import csv
import sys

db = SQL("sqlite:///students.db")


with open(sys.argv[1], "r") as csv_file:
    
    db.execute("DELETE FROM students")
    
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        
        person_name = row['name'].split(" ")
        
        a = person_name[0]
        b = person_name[1]
        d = row['house']
        e = int(row['birth'])
        
        if len(person_name) == 3:
            
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", a, b, person_name[2], d, e)
        
        else:
            
            db.execute("INSERT INTO students (first, last, house, birth) VALUES (?, ?, ?, ?)", a, b, d, e)
