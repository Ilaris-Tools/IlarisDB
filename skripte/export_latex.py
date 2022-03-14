import pylatex
from pylatex.base_classes import Arguments as A
from pylatex import Command as C
from pylatex.utils import NoEscape as NE
import interface as db


def kreaturcommand(id, name, bes, klasse, kasten):
    cmd = f"\kreatur{id}"
    args = A(name, bes, f"gfx/kreaturen/{klasse}", NE(kasten))
    runs = C("kreatur", arguments=args).dumps()
    return C('newcommand', NE(cmd), extra_arguments=[NE(runs)]).dumps()


def quellenangabe(k, quellen):
    q = quellen.get(k.get("quelle"), {}).get("name")
    if q:
        k["beschreibung"] += f" (Quelle: {q})"


def mehrzeiler(zeilen):
    if zeilen:
        return ["".join(zeilen)]
    return []


def kinfo(k, v):
    return C("kreaturinfo", A(k, v)).dumps()


def fertigliste(ferts):
    fertstr = [
        f"{f.get('name', '')} {f.get('wert', '')}".strip() for f in ferts]
    return ", ".join(fertstr)


def vorteilliste(vorts):
    vs = []
    for v in vorts:
        vstr = v['name']
        if 'info' in v:
            vstr += f"({v['info']})"
        vs.append(vstr)
    return ", ".join(vs)


def tps(w):
    tp = w.get('TP', '')
    if not tp:
        return tp
    return f"{tp['anzahl']}W{tp['W']}{tp.get('plus', 0):+}"


def b_werte(k):
    w = k.get("kampf", {}).get("werte", None)
    if not w:
        return []
    args = A(w.get('WS', ''), w.get('MR', ''),
             w.get('GS', ''), w.get('INI', ''))
    return [C("kreaturkampfwerte", args).dumps()]


def b_eigenschaften(k):
    if not "eigenschaften" in k:
        return []
    eigenschaften = ', '.join([v.get('name') for v in k["eigenschaften"]])
    return [f"\\kreaturvorteile{{{eigenschaften}}}"]


def b_kampf(k):
    zeilen = []
    vorteile = k.get("kampf", {}).get("vorteile")
    waffen = k.get("kampf", {}).get("waffen")
    if waffen:
        for w in waffen:
            args = A(w.get('name', ''), w.get('RW', ''), w.get(
                'VT', ''), w.get('AT', ''), tps(w), w.get('info', ''))
            zeilen.append(C("kreaturwaffe", args).dumps())
    if vorteile:
        txt = ', '.join([v['name'] for v in vorteile])
        zeilen.append(C("kreaturkampfvorteile", A(txt)).dumps())
    print(zeilen)
    return mehrzeiler(zeilen)


def b_profan(k):
    talente = k.get("talente")
    attribute = k.get("attribute")
    freieferts = k.get("freiefertigkeiten")
    vorteile = k.get("profan", {}).get("vorteile")
    zeilen = []
    if attribute:
        attr = ", ".join([f"{a} {v}" for a, v in attribute.items()])
        zeilen.append(C("kreaturattribute", A(attr)).dumps())
    if talente:
        zeilen.append(C("kreaturfertigkeiten", A(
            fertigliste(talente))).dumps())
    if freieferts:
        zeilen.append(C("kreaturfertigkeiten", A(
            fertigliste(freieferts))).dumps())
    if vorteile:
        zeilen.append(
            C("kreaturinfo", A("Profane Vorteile", vorteilliste(vorteile))).dumps())
    return mehrzeiler(zeilen)


def b_uebernat(k, key="magie", energy="AsP", vname="Magische Vorteile"):
    data = k.get(key)
    if not data:
        return []
    fts = data.get("fertigkeiten")
    vts = data.get("vorteile")
    res = data.get(energy.lower())
    zeilen = []
    if res:
        zeilen.append(f"\\kreaturinfo{{{energy}}}{{{res}}}")
    if fts:
        for f in fts:
            txt = f"{f.get('wert', '')}"
            talente = ", ".join([t['name'] for t in f.get("talente", [])])
            if talente:
                txt += f" ({talente})"
            zeilen.append(
                C("kreaturinfo", A(f['name'], txt)).dumps())
    if vts:
        txt = vorteilliste(vts)
        zeilen.append(C("kreaturinfo", A(vname, txt)).dumps())
    return mehrzeiler(zeilen)


def b_beschwoerung(k):
    beschwoer = k.get("beschwoerung")
    if not beschwoer:
        return []
    proben = beschwoer.get("proben")
    dienste = beschwoer.get("dienste")
    zeilen = []
    if proben:
        ps = []
        for p in proben:
            pss = p['name']
            kosten = p.get('kosten')
            mod = p.get('mod')
            if kosten or mod:
                pss += "("
                if mod:
                    if mod > 0:
                        pss += f"+{mod}"
                    else:
                        pss += f"-{mod}"
                if mod and kosten:
                    pss += ", "
                if kosten:
                    pss += f"{kosten} AsP"
                pss += ")"
            ps.append(pss)
        zeilen.append(kinfo("Beschwörung", ', '.join(ps)))
    if dienste:
        ds = []
        for d in dienste:
            dss = d['name']
            mod = d.get('mod', 0)
            if not mod:
                mod = 0
            dss += f"{mod:+}"
            if "dauer" in d:
                dss += f" ({d['dauer']})"
            ds.append(dss)
        zeilen.append(kinfo("Dienste", ', '.join(ds)))
    return mehrzeiler(zeilen)


def b_info(k):
    if not "info" in k:
        return []
    return [C("kreaturinfo", A('Info', k['info'])).dumps()]


def b_infos(k):
    if not "infos" in k:
        return []
    zeilen = []
    for i in k["infos"]:
        zeilen.append(kinfo(i.get("name", ""), i.get("info", "")))
    return mehrzeiler(zeilen)


def b_sonstiges(k):
    sonst = k.get("sonstiges")
    if not sonst:
        return []
    block = ""
    for name, text in sonst.items():
        block += kinfo(name, text)
    return [block]


def kreaturkasten(k):
    bloecke = []
    bloecke.extend(b_werte(k))
    bloecke.extend(b_eigenschaften(k))
    bloecke.extend(b_kampf(k))
    bloecke.extend(b_profan(k))
    bloecke.extend(b_uebernat(k))  # default magie
    bloecke.extend(b_uebernat(k, vname="Karmale Vorteile",
                   energy="KaP", key="karma"))
    bloecke.extend(b_uebernat(k, vname="Paktvorteile",
                   energy="GuP", key="pakt"))
    bloecke.extend(b_beschwoerung(k))
    bloecke.extend(b_info(k))
    bloecke.extend(b_infos(k))
    bloecke.extend(b_sonstiges(k))
    return "\\trennlinie ".join(bloecke)


def main():
    kreaturen = db.load("kreaturen")
    quellen = db.load("quellen")
    commands = []
    klassen = {}
    # krearium = pylatex.Document(documentclass="Ilaris")
    for id, k in kreaturen.items():
        quellenangabe(k, quellen)
        kasten = kreaturkasten(k)
        commands.append(kreaturcommand(
            id, k['name'], k['beschreibung'], k['klasse'], kasten))
        # kreaturarium
        if not k["klasse"] in klassen:
            klassen[k["klasse"]] = []
        klassen[k["klasse"]].append(f"\kreatur{id}")
    with open("../export/latex/kreaturen.tex", "w") as wf:
        wf.write("\n".join(commands))
    with open("../export/latex/kreaturarium.tex", "w") as bfile:
        tex = """
\documentclass{Ilaris}
\input{kreaturen.tex}
\\begin{document}
\spaltenanfang
"""
        for k, v in klassen.items():
            tex += f"\skapitel{{{k}}}\n"
            tex += "\n".join(v)
        tex += "\n\spaltenende\n\end{document}"
        bfile.write(tex)


if __name__ == "__main__":
    main()
