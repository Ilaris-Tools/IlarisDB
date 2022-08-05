""" WIP dont use
hack and dirty script um systematisch alle einträge anzupassen.
Achtung die kreature.yaml file wird direkt überschrieben,
ist nur ein Hilfsmittel zum Erstmaligen Aufbau der DB
"""

import yaml
import interface as db


# with open("../daten/kreaturen_neu.yml", "r") as kbak:
#     kreaturen = yaml.load(kbak)


# reqkeys = ["name", "beschreibung", "id"]
# optkeys = ["waffen", "kampfwerte", "vorteile", "astral", "karmal",
#            "pakt", "attribute", "info", "besonderheiten", "beschwörung"]


def restore_key(k, key):
    kbak = kreaturen_bak[k["id"]]
    val = kbak.get(key, False)
    if not val:
        del(k[key])
    else:
        k[key] = val


def fix_id(k, i):
    if not "id" in k:
        k["id"] = i


def fix_vorteile(k):
    keys = ["vorteile", "profanvorteile", "kampfvorteile"]
    vkey = keys[0]
    if not vkey in k:
        print("keine keys")
        return
    if "name" in k[vkey][0]:
        print("schon fertig")
        return
    vorteile = []
    for v in k[vkey]:
        vort = {}
        vort["name"] = v
        vorteile.append(vort)
    if len(vorteile) > 0:
        k[vkey] = vorteile
        print("...")


def fix_profan_vorteile(k):
    if "profanvorteile" in k:
        if not "profan" in k:
            k["profan"] = {}
        k["profan"]["vorteile"] = k["profanvorteile"]
        del(k["profanvorteile"])


def fix_kampf_vorteile(k):
    kv = "kampfvorteile"
    if kv in k:
        if not "kampf" in k:
            k["kampf"] = {}
        k["kampf"]["vorteile"] = k[kv]
        del(k[kv])


def fix_waffen(k):
    if "waffen" in k:
        if not "kampf" in k:
            k["kampf"] = {}
        k["kampf"]["waffen"] = k["waffen"]
        del(k["waffen"])


def fix_astral(k):
    if "astral" in k:
        k["magie"] = k["astral"]
        del(k["astral"])


def fix_kampfwerte(k):
    if "kampfwerte" in k:
        if not "kampf" in k:
            k["kampf"] = {}
        k["kampf"]["werte"] = k["kampfwerte"]
        del(k["kampfwerte"])


def fix_werte_int(k):
    if "kampf" in k:
        if "werte" in k["kampf"]:
            for ww in ["GS", "INI"]:
                if ww in k["kampf"]["werte"]:
                    try:
                        k["kampf"]["werte"][ww] = int(k["kampf"]["werte"][ww])
                    except:
                        pass
        if "waffen" in k["kampf"]:
            for w in k["kampf"]["waffen"]:
                for ww in ["TPW", "TPP", "TPW20"]:
                    try:
                        w[ww] = int(w[ww])
                    except:
                        continue


def fix_talente(k):
    if "magie" in k:
        if "fertigkeiten" in k["magie"]:
            for fert in k["magie"]["fertigkeiten"]:
                fert["talente"] = [{"name": t} for t in fert["talente"]]


def fix_sonstiges(k):
    for nk in ["beispieldienste", "beschwörung", "schwachpunkte", "vorgehen"]:
        if nk in k:
            if not "sonstiges" in k:
                k["sonstiges"] = {}
            k["sonstiges"][nk] = k[nk]
            del(k[nk])


def sep_varianten(kreaturen):
    neuek = {}
    for k in kreaturen.values():
        print(k["name"])
        if "varianten" in k:
            for v in k["varianten"]:
                if not v["id"] in kreaturen:
                    print(f'erstelle variante: {v["id"]}')
                    nv = k.copy()
                    nv["unterschied"] = v.get("unterschied", "")
                    nv["variantevon"] = k["id"]
                    del(nv["varianten"])
                    neuek[v["id"]] = nv
    for ke, va in neuek.items():
        if not ke in kreaturen:
            kreaturen[ke] = va
        else:
            print("schon drin")


def default_klasse(k):
    if not "klasse" in k:
        k["klasse"] = "tier"


def fix_waffen_tp(k):
    waffen = k.get("kampf", {}).get("waffen")
    if not waffen:
        return
    for w in k["kampf"]["waffen"]:
        if "TP" in w and not "TPP" in w:
            if w["TP"].__contains__("W6+"):
                tpps = w["TP"].split("W6+")
                w["TPP"] = tpps[1]
                w["TPW"] = tpps[0]
            elif w["TP"].__contains__("W20+"):
                tpps = w["TP"].split("W20+")
                w["TPP"] = tpps[0]
                w["TPW20"] = tpps[1]
            elif w["TP"].__contains__("W6"):
                tpps = w["TP"].split("W6")
                w["TPP"] = 0
                w["TPW"] = tpps[0]
            elif w["TP"].__contains__("W20"):
                tpps = w["TP"].split("W20")
                w["TPP"] = 0
                w["TPW20"] = tpps[0]
            else:
                print(f"ERROR: {w['TP']}")


def fix_tp_int(k):
    for w in k["kampf"]["waffen"]:
        if "TPP" in w:
            w["TPP"] = int(w["TPP"])
        if "TPW" in w:
            w["TPW"] = int(w["TPW"])
        if "TPW20" in w:
            w["TPW20"] = int(w["TPW20"])


def remove_id(k):
    if "id" in k:
        del(k["id"])


def split_tp(k):
    if not "kampf" in k:
        return
    if not "waffen" in k["kampf"]:
        return
    for w in k["kampf"]["waffen"]:
        if not "TPP" in w:
            print("KEIN TPP")
            continue
        tp = {}
        tp["plus"] = w["TPP"]
        if "TPW" in w:
            tp["W"] = 6
            tp["anzahl"] = w["TPW"]
            del(w["TPW"])
        if "TPW20" in w:
            tp["W"] = 20
            tp["anzahl"] = w["TPW20"]
            del(w["TPW20"])
        w["TP"] = tp
        # del(w["TPP"])


def fix_eigenschaften(k):
    if "vorteile" in k:
        k["eigenschaften"] = k["vorteile"]


def rm_vorteile(k):
    if "vorteile" in k:
        del(k["vorteile"])


def beispieldienste(k):
    bda = k.get("sonstiges", {}).get("beispieldienste")
    if not bda:
        return
    neu = []
    for bd in bda:
        bdn = {"name": bd}
        neu.append(bdn)
    k["sonstiges"]["dienste"] = neu


def dienste(k):
    bda = k.get("sonstiges", {}).get("beispieldienste")
    if not bda:
        return
    k["sonstiges"]["dienste"] = bda
    del(k["sonstiges"]["beispieldienste"])


def refix_eigenschaften(k):
    if not "eigenschaften" in k:
        return
    for e in k["eigenschaften"]:
        extras = []
        if "info" in e:
            if not "id" in e:
                id = e["name"].lower()
                uml = {"ä": "ae", "ü": "ue", "ö": "oe",
                       "ß": "ss", " ": "", "(": "", ")": ""}
                for xx, yy in uml.items():
                    id = id.replace(xx, yy)
                e["id"] = id
            extras.append(e.pop("info"))
        if "stufe" in e:
            extras.append(e.pop("stufe"))
        if extras:
            e["name"] = e["name"] + "(" + ", ".join(extras) + ")"


def refix_eigenschaften2(k):
    if not "eigenschaften" in k:
        return
    for e in k["eigenschaften"]:
        if "id" in e and not "name" in e:
            e["name"] = e["id"]
        if "name" in e and not "id" in e and not "(" in e["name"]:
            id = e["name"].lower()
            uml = {"ä": "ae", "ü": "ue", "ö": "oe",
                   "ß": "ss", " ": "", "(": "", ")": ""}
            for xx, yy in uml.items():
                id = id.replace(xx, yy)
            e["id"] = id


def vorteile_zu_eigenschaften(k):
    if not "kampf" in k:
        return
    if not "vorteile" in k["kampf"]:
        return
    for vt in k["kampf"]["vorteile"]:
        if not "Zusätzlich" in vt['name']:
            continue
        # print("found: ")
        print(k['name'])
        eig = {"name": vt['name'], "id": "zusaetzlicheattacke"}
        if not "eigenschaften" in k:
            k["eigenschaften"] = []
        k['eigenschaften'].append(eig)
        k["kampf"]["vorteile"].remove(vt)


fname = "kreaturen"
kreaturen = db.load(fname)
for i, k in kreaturen.items():
    # print(i)
    # if i == "ghul2":
    #     continue
    # if k.get("quelle") != "hilberts":
    #     continue
    # if k["klasse"] == "tier" or k["klasse"] == "elementar":
    #     try:
    #         if "attribute" in k:
    #             if "KO" in k["attribute"]:
    #                 k["attribute"]["KO"] = k["attribute"]["KO"]*2
    #             if "KK" in k["attribute"]:
    #                 k["attribute"]["KK"] = k["attribute"]["KK"]*2
    #         print(k["name"] + " erfolg")
    #     except Exception as e:
    #         print(k["name"] + "fehler")
    #         print(e)

    # dienste(k)

    # k["fertigkeiten"] = talente
    # sep_varianten(kreaturen)
    # print(len(kreaturen.keys()))
    # refix_eigenschaften2(k)
    vorteile_zu_eigenschaften(k)
db.save(fname, kreaturen)
