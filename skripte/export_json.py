import json
import interface as db

with open("../export/json/kreaturen.json", "w") as jfile:
    json.dump(db.load("kreaturen"), jfile, indent=2, ensure_ascii=False)
