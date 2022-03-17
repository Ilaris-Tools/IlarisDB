import json
import interface as db


def export_json(tabelle):
    with open(f"../export/json/{tabelle}.json", "w") as jfile:
        json.dump(db.load(tabelle), jfile, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    export_json("kreaturen")
