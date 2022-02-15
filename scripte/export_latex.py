import yaml
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
}  # todo: in eigene yaml file verschieben?


with open("../daten/kreaturen.yml", "r") as kfile:
    kreaturen = yaml.load(kfile)
for id, k in kreaturen.items():
    bloecke = []
    if "kampfwerte" in k:
        w = k['kampfwerte']
        bloecke.append(
            f"\\kreaturkampfwerte{{{w['WS']}}}{{{w['MR']}}}{{{w['GS']}}}{{{w['INI']}}}")
    if "vorteile" in k:
        # ohne weitere formatierung
        bloecke.append(f"\\kreaturvorteile{{{', '.join(k['vorteile'])}}}")
    if "waffen" in k or "kampfvorteile" in k:
        block = ""
        if "waffen" in k:
            for w in k['waffen']:
                block += f"\\kreaturwaffe{{{w['name']}}}{{{w.get('RW', '')}}}{{{w.get('VT','')}}}{{{w.get('AT','')}}}{{{w.get('TP','')}}}{{{w.get('bemerkung', '')}}}"
        if "kampfvorteile" in k:
            block += f"\\kreaturkampfvorteile{{{', '.join(k['kampfvorteile'])}}}"
        bloecke.append(block)
    if "fertigkeiten" in k or "attribute" in k:
        block = ""
        if "attribute" in k:
            attr = ", ".join([f"{a} {v}" for a, v in k['attribute'].items()])
            block += f"\\kreaturattribute{{{attr}}}"
        if "fertigkeiten" in k:
            fert = ", ".join(
                [f"{a} {v}" for a, v in k['fertigkeiten'].items()])
            block += f"\\kreaturfertigkeiten{{{fert}}}"
        bloecke.append(block)
    if "varianten" in k:
        varn = '\\\\'.join(k['varianten'])
        bloecke.append(f"\\kreaturvarianten{{{varn}}}")

    output += textemplate.substitute(
        id=id,
        name=k['name'],
        klasse=k.get('klasse', 'humanoid'),
        body="\\trennlinie".join(bloecke),
        beschreibung=k.get('beschreibung'))
with open("../export/latex/kreaturen.tex", "w") as tfile:
    tfile.write(output)
