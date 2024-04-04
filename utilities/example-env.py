SECRET_KEY = ""
DB_USER = ""
DB_PASS = ""
DB_HOST = ""
DB_NAME = ""
DB_URI = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
URL = ""
TOKEN = ""
ID = ""
PASSWORD = ""
TOKEN_XPATH = ""
GRADE_XPATH = ""
MAX = {"TOTAL": {"SEM9": 450, "SEM8": 500, "SEM7": 500, "SEM6": 450,
                 "SEM5": 475, "SEM4": 500, "SEM3": 500, "SEM2": 500,
                 "SEM1": 400},
       "SEM9": {"ENT": 100, "EBMR": 50, "OPTH": 150, "FMIMC": 150},
       "SEM8": {"OGYN2": 175, "PED2": 175, "MED3": 75, "SURG3": 75},
       "SEM7": {"surg2": 75, "MED2": 75, "PED1": 175, "OGYN1": 175},
       "SEM6": {"COM": 150, "SURG1": 150, "MED1": 150},
       "SEM5": {"FCT": 125, "RLM": 50, "DERM": 100, "PSYC": 100, "BMSP": 100},
       "SEM4": {"_1104": 500},
       "SEM3": {"_1103": 500},
       "SEM2": {"_1102": 500},
       "SEM1": {"_1101": 400}
       }
