import yaml
import interface as db
from string import Template

textemplate = Template("""
\\newcommand{\kreatur$id}{\kreatur{$name}{$beschreibung}{kreaturen/$klasse}{
    $body
}}""")


output = ""

kampfwertkeys = {
    "MR": "Magieresistenz",
    "WS": "Wundschwelle",
    "GS": "Geschwindigkeit",
    "INI": "Initiative",
}


def block_kampfwerte(k):
    w = k.get("kampf", {}).get("werte", None)
    if not w:
        return []
    return [f"\\kreaturkampfwerte{{{w.get('WS', '')}}}{{{w.get('MR', '')}}}{{{w.get('GS', '')}}}{{{w.get('INI', '')}}}"]


def block_vorteile(k):
    if not "vorteile" in k:
        return []
    vorteile = ', '.join([v.get('name') for v in k["vorteile"]])
    return [f"\\kreaturvorteile{{{vorteile}}}"]


def block_kampf(k):
    vorteile = k.get("kampf", {}).get("vorteile")
    waffen = k.get("kampf", {}).get("waffen")
    if not waffen and not vorteile:
        return []
    block = ""
    if waffen:
        for w in waffen:
            block += f"\\kreaturwaffe{{{w.get('name', '')}}}{{{w.get('RW', '')}}}{{{w.get('VT', '')}}}{{{w.get('AT','')}}}{{{w.get('TP','')}}}{{{w.get('bemerkung', '')}}}"
    if vorteile:
        block += f"\\kreaturkampfvorteile{{{', '.join([v['name'] for v in vorteile])}}}"
    return [block]


def block_attribute_und_fertigkeiten(k):
    fertigkeiten = k.get("fertigkeiten")
    attribute = k.get("attribute")
    if not fertigkeiten and not attribute:
        return []
    block = ""
    if attribute:
        attr = ", ".join([f"{a} {v}" for a, v in k['attribute'].items()])
        block += f"\\kreaturattribute{{{attr}}}"
    if fertigkeiten:
        fertstr = [
            f"{f.get('name', '')} {f.get('wert', '')}" for f in fertigkeiten]
        fert = ", ".join(fertstr)
        block += f"\\kreaturfertigkeiten{{{fert}}}"
    return [block]


def block_sonstiges(k):
    sonst = k.get("sonstiges")
    if not sonst:
        return []
    block = ""
    for name, text in sonst.items():
        block += f"\\keraturinfo{{{name}}}{{{text}}}"
    return [block]


kreaturen = db.load("kreaturen")
for id, k in kreaturen.items():
    bloecke = []
    # kampfwert block
    bloecke.extend(block_kampfwerte(k))
    bloecke.extend(block_vorteile(k))
    bloecke.extend(block_kampf(k))
    bloecke.extend(block_attribute_und_fertigkeiten(k))
    bloecke.extend(block_sonstiges(k))

    output += textemplate.substitute(
        id=id,
        name=k['name'],
        klasse=k['klasse'],
        body="\\trennlinie".join(bloecke),
        beschreibung=k.get('beschreibung'))
with open("../export/latex/kreaturen.tex", "w") as tfile:
    tfile.write(output)
