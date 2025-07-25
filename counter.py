#diesel_Counter
#record fuel with given timestamp

data = {
    "generators": {
        "Zone 1": True,
        "Zone 2": False,
        "Zone 3": False,
        "Zone 4": False
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

import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%H, %M, %S"))







            


