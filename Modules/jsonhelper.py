import json


def writeJ(content, file:str, indent:int = 2, encoding:str = 'utf-8') -> None:
    with open(file, "w", encoding = encoding) as f:
        json.dump(content, f, indent=indent, ensure_ascii=False)

def readJ(file:str, encoding:str = 'utf-8') -> dict:
    json_file = open(file, "r", encoding = encoding)
    content = json.load(json_file)
    json_file.close()
    return content

def convertDict(string:str) -> dict:
    content = json.loads(string)
    return content

def convertStr(dictionary:dict, indent:int = 2) -> str:
    content = json.dumps(dictionary, indent = indent)
    return content

def dictSorting(dictionary:dict) -> dict:
    content = json.dumps(dictionary, indent=4, sort_keys=True)
    return convertDict(content)