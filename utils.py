from json import load, dump

def list_to_string(list):
    return ''.join(list)

def read_json(path, encoding):
    with open(path, encoding=encoding) as json_file:
        open_json_file = load(json_file)
    return open_json_file

def write_json(data, path, encoding):
    with open(path, 'w', encoding=encoding) as json_file:
        dump(data, json_file, ensure_ascii=False, indent=4)

config = read_json('config.json', 'utf-8')