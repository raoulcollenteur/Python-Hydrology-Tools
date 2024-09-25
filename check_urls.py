import json

import requests


def check_urls(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    broken_urls = []

    for package, details in data.items():
        url = details.get("url")
        if url:
            try:
                response = requests.head(url, allow_redirects=True)
                if response.status_code != 200:
                    broken_urls.append((package, url, response.status_code))
            except requests.RequestException as e:
                broken_urls.append((package, url, str(e)))

    return broken_urls


if __name__ == "__main__":
    broken_urls = check_urls("list.json")
    if broken_urls:
        print("Broken URLs found:")
        for package, url, status in broken_urls:
            print(f"{package}: {url} (Status: {status})")
        exit(1)
    else:
        print("All URLs are working.")
        exit(0)
