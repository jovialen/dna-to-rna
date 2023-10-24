import json
import csv


def read_json(path: str) -> json:
    """Read a JSON file

    Args:
        path (str): Path to the JSON file

    Returns:
        json: The read JSON file
    """
    
    with open(path, "r") as f:
        return json.load(f)


def read_csv(path: str, delimiter: str = ";", quote: str = "\"") -> csv:
    """Read a CSV file

    Args:
        path (str): Path to the CSV file
        delimiter (str, optional): The character to separate fields. Default is ;
        quote (str, optional): The character to surround text. Default is "

    Returns:
        csv: The read CSV file
    """
    
    with open(path, "r") as f:
        data = csv.reader(f, delimiter=delimiter, quotechar=quote)
        return list(data)


def read_csv_to_dict(path: str, delimiter: str = ";", quote: str = "\"") -> dict:
    """Read a CSV file to a dictionary

    Args:
        path (str): Path to the CSV file
        delimiter (str, optional): The character to separate fields. Default is ;
        quote (str, optional): The character to surround text. Default is "

    Returns:
        dict: The dictionary from the CSV file
    """
    
    data = read_csv(path, delimiter=delimiter, quote=quote)
    field_names = data[0]
    data_dict = {}
    
    for row in data[1:]:
        fields = {}
        for i, field in enumerate(row[1:]):
            fields[field_names[i + 1]] = field
        data_dict[row[0]] = fields
    
    return data_dict


def read_text(path: str) -> str:
    with open(path, "r") as f:
        return f.read().replace("\n", "")