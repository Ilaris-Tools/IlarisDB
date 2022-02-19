import yaml
import yamale


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def load(table):
    with open(f"../daten/{table}.yml", "r") as table_file:
        table_data = yaml.load(table_file)
    return table_data


def validate(table, data=None):
    schema = yamale.make_schema(f'../schemata/{table}.yml')
    if data is None:
        data = yamale.make_data(f'../daten/{table}.yml')
    yamale.validate(schema, data, strict=True)
    print("\nYaY! Datei ist ok :)")
    return True


def save(table, data, validate=False):
    if validate:
        validate(table, data)
    dump = yaml.dump(data, default_flow_style=False,
                     allow_unicode=True, Dumper=NoAliasDumper)
    with open(f"../daten/{table}.yml", "w", encoding='utf8') as table_file:
        table_file.write(dump)
