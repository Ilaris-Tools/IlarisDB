import yaml
from string import Template

textemplate = Template("""
\\newcommand{\kreatur$id}{\kreatur{$name}{$beschreibung}{kreaturen/$klasse}{
    $body
}}""")

output = ""

with open("../daten/kreaturen.yml", "r") as kfile:
    kreaturen = yaml.load(kfile)
for id, k in kreaturen.items():
    # die zeilen sind optional daher erstmal manuell durchgehen, vlt. spaeter in elegant
    body = ""
    if "kampfwerte" in k:
        nl = '\\\\'
        body += f"\kreaturinfo{{Kampfwerte}}{{{nl.join([str(x) for x in k['kampfwerte'].items()])}}}"

    output += textemplate.substitute(
        id=id, name=k['name'], klasse=k.get('klasse', 'humanoid'), body=body, beschreibung=k.get('beschreibung'))
with open("../export/latex/kreaturen.tex", "w") as tfile:
    tfile.write(output)
