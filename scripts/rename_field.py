import json


def add_entry(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    for package in data.values():
        package["legacy"] = ""

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    add_entry("list.json")
