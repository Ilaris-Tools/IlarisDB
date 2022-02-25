import yamale
schema = yamale.make_schema('../schemata/kreaturen.yml')
data = yamale.make_data('../daten/kreaturen.yml')
print(f"Prüfe {len(data[0][0].keys())} Kreaturen:")
yamale.validate(schema, data, strict=True)
print("\nYaY! Datei ist ok :)")
