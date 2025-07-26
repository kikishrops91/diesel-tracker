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
        "Komatsu PC210": False,
        "Komatsu PC360": False,
        "Komatsu PC135": False,
    },
    "hyundai": {
        "Hyundai HX140l": False,
        "Hyundai LC140": False,
        "Hyundai HX235": False
    },
    "Jcb": {
        "Jcb 14T": False
    },
    "Volvo": {
        "Volvo A30G": False,
        "Volvo A25G": False,
        "Volvo A40G": False
    },
    "Liebherr": {
        "Liebherr 1550": False
    },
    "New Holland": {
        "New Holland T6": False
    }
        }

con = sqlite3.connect("data/fuel_data.db")
cur = con.cursor()


# Create table if it doesn't exist
cur.execute("""
CREATE TABLE fuel (
    name TEXT,
    location TEXT,
    litres INTEGER,
    date TEXT,
    operator TEXT,
    PRIMARY KEY (name, location, date)
)
""")

# Insert initial data
fuel_data = [
    ("Generator", "Zone 1", 34, "25/07/2025", "Null"),
    ("Generator", "Zone 2", 43, "25/07/2025", "Null"),
    ("Generator", "Zone 3", 46, "25/07/2025", "Null"),
    ("Generator", "Zone 4", 45, "25/07/2025", "Null"),
    ("Komatsu PC210", "Zone 1", 322, "26/07/2025", "Phil"),
    ("Komatsu PC360", "Zone 2", 323, "26/07/2025", "Nial"), 
    ("Komatsu PC135", "Zone 3", 23, "26/07/2025", "Vic"),
    ("Hyundai HX140l", "Zone 1", 452, "26/07/2025", "Andy"),
    ("Hyundai LC140", "Zone 3", 333, "26/07/2025", "Lou"),
    ("Hyundai HX235", "Zone 2", 470, "26/07/2025", "Mark"),
    ("Jcb 14T", "Zone 4", 309, "26/07/2025", "Gareth"),
    ("Volvo A30G", "Zone 1", 200, "26/07/2025", "Bob"),
    ("Volvo A25G", "Zone 1", 250, "26/07/2025", "Penny"),
    ("Volvo A40G", "Zone 1", 300, "26/07/2025", "Jim"),
    ("Leibherr 1550", "Zone 1", 402, "26/07/2025", "Frank"),
    ("New Holland T6", "Zone 2", 240, "26/07/2025", "George"),

]



con.commit()


x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%H, %M, %S"))










