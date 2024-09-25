import json


def generate_list():
    with open("list.json", "r") as file:
        data = json.load(file)

    with open("README.md", "w") as file:
        file.write("# Open Source Python Packages in Hydrology\n")
        file.write(
            "My attempt to list interesting open source python projects that can be used in the field of Hydrology. Suggestions as issues or pull requests are welcome!\n\n"
        )
        file.write(
            'UPDATE: The Pypa package authority has now added ["Hydrology" as a classifier](https://github.com/pypa/warehouse/issues/5728) so we can start [collecting python packages](https://pypi.org/search/?q=&o=&c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Hydrology) used by the hydrological community! If you are maintaining a python package, please add `Topic :: Scientific/Engineering :: Hydrology` to your setup.py so people can find your package.\n\n'
        )
        file.write("Raoul A. Collenteur, Eawag.\n\n")

        categories = {}
        for package_name, package in data.items():
            category = package["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((package_name, package))

        for category, packages in categories.items():
            file.write(f"## {category}\n")
            file.write(
                "| Project Name | Description (Longer Header to Widen Column) | PyPI Conda | Docs | CI | Paper |\n"
            )
            file.write(
                "| ------------ | ------------------------------------------ | ---------- | ---- | -- | --------- |\n"
            )
            for package_name, package in packages:
                description = package["description"]
                url = package["url"]
                pypi_url = package.get("pypi", "")
                conda_url = package.get("conda", "")
                docs_url = package.get("docs", "")
                ci_status = package.get("CI", 0)
                version = package.get("version", "")
                last_update = package.get("last_update", "")
                doi_paper = package.get("doi_paper", "")

                if version or last_update:
                    description += f" (Version: {version}, Last Update: {last_update})"

                pypi_logo = (
                    f"[![PyPI](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white)]({pypi_url})"
                    if pypi_url
                    else ""
                )
                conda_logo = (
                    f"[![Conda](https://img.shields.io/badge/-44A833?logo=anaconda&logoColor=white)]({conda_url})"
                    if conda_url
                    else ""
                )
                docs_logo = (
                    f"[![Docs](https://img.shields.io/badge/-217346?logo=readthedocs&logoColor=white)]({docs_url})"
                    if docs_url
                    else ""
                )
                ci_logo = (
                    "[![CI](https://img.shields.io/badge/CI-passing-brightgreen)]"
                    if ci_status
                    else ""
                )
                doi_paper_logo = (
                    f"[![DOI](https://img.shields.io/badge/DOI-10.1000/xyz123-blue)]({doi_paper})"
                    if doi_paper
                    else ""
                )

                file.write(
                    f"| [{package_name}]({url}) | {description} | {pypi_logo} {conda_logo} | {docs_logo} | {ci_logo} | {doi_paper_logo} |\n"
                )
            file.write("\n")


if __name__ == "__main__":
    generate_list()