import yamale
schema = yamale.make_schema('../schemata/kreaturen.yml')
data = yamale.make_data('../daten/kreaturen.yml')
yamale.validate(schema, data, strict=True)
print("\nYaY! Datei ist ok :)")
