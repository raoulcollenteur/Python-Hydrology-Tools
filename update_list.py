import json

import requests


def get_pypi_info(package_name):
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        if response.status_code == 200:
            data = response.json()
            version = data["info"]["version"]
            last_update = data["releases"][version][0]["upload_time"]
            return version, last_update
    except Exception as e:
        print(f"Error fetching PyPI info for {package_name}: {e}")
    return None, None


def get_conda_info(package_name):
    try:
        response = requests.get(
            f"https://api.anaconda.org/package/conda-forge/{package_name}"
        )
        if response.status_code == 200:
            data = response.json()
            version = data["latest_version"]
            last_update = data.get("latest_upload", "")
            return version, last_update
    except Exception as e:
        print(f"Error fetching Conda info for {package_name}: {e}")
    return None, None


def update_list(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    for package_name, package_info in data.items():
        pypi_url = package_info.get("pypi", "")
        conda_url = package_info.get("conda", "")

        pypi_version, pypi_last_update = None, None
        conda_version, conda_last_update = None, None

        if pypi_url:
            pypi_package_name = pypi_url.split("/")[-2]
            pypi_version, pypi_last_update = get_pypi_info(pypi_package_name)

        if conda_url:
            conda_package_name = conda_url.split("/")[-1]
            conda_version, conda_last_update = get_conda_info(conda_package_name)

        # Determine the latest version and last update date
        version = pypi_version or conda_version
        last_update = max(
            filter(None, [pypi_last_update, conda_last_update]), default=""
        )

        if version:
            package_info["version"] = version
        if last_update:
            package_info["last_update"] = last_update

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    update_list("list.json")
