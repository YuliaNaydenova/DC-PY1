import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        data_ = f.read()
        lists = (data_.split(new_line))[:-1]
        sep_lists = [i.split(delimiter) for i in lists]
        columns, strings = len(sep_lists[0]), len(sep_lists)-1
        dicts = [{} for i in range(strings)]
        for i in range(strings):
            for j in range(columns):
                dicts[i][sep_lists[0][j]] = sep_lists[i+1][j]
        return dicts

# TODO реализовать конвертер из csv в json

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
