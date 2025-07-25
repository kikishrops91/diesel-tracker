import datetime
import sqlite3

#diesel_Counter
#record fuel with given timestamp

data = {
    "generators": {
        "Gen Zone 1": False,
        "Gen Zone 2": False,
        "Gen Zone 3": False,
        "Gen Zone 4": False
    },
    "komatsu": {
        "komatsu pc210": False,
        "komatsu pc360": False,
        "komatsu pc135": False,
    },
    "hyundai": {
        "hyundai hx140l": False,
        "hyundai lc140": False,
        "hyundai hx235": False
    },
    "jcb": {
        "jcb lc151_t": False
    },
    "volvo": {
        "volvo a30g": False,
        "volvo a25d": False,
        "volvo a40g": False
    },
    "liebherr": {
        "liebherr 1550": False
    },
    "new holland": {
        "new holland t6": False
    }
        }

con = sqlite3.connect("data/fuel_data.db")
cur = con.cursor()

cur.execute("CREATE TABLE fuel (name TEXT PRIMARY KEY, LOCATION text, litres INTEGER, date TEXT, operator TEXT)")
cur.execute("""
INSERT INTO fuel VALUES
            ("Generator", "Zone 1", 34, "25/07/2025", "Null"),
            ("Generator", "Zone 2", 43, "25/07/2025", "Null"),
            ("Generator", "Zone 3", 46, "25/07/2025", "Null"),
            ("Generator", "Zone 4", 45, "25/07/2025", "Null"),

            
""")

con.commit()


x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%H, %M, %S"))







            


