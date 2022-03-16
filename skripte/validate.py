import yamale
import sys
import interface as db

table = "kreaturen"
schemaf = "kreaturen"
if len(sys.argv) > 1:
    table = sys.argv[1]
if len(sys.argv) > 2:
    schemaf = sys.argv[2]


db.validate(table, schemaf=schemaf)
# print(f"Prüfe {len(data[0][0].keys())} Kreaturen:")
# schema = yamale.make_schema('../schemata/kreaturen.yml')
# data = yamale.make_data('../daten/kreaturen_neu2.yml')
# yamale.validate(schema, data, strict=True)
# print("\nYaY! Datei ist ok :)")
