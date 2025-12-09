import os
import re
import zipfile
import argparse
import requests
from io import BytesIO

def clone_github_folder(folder_url, output_dir):
    # Parse URL
    m = re.match(r"https://github.com/([^/]+)/([^/]+)/tree/([^/]+)/(.*)", folder_url)
    if not m:
        raise ValueError("Invalid GitHub folder URL")

    user, repo, branch, folder_path = m.groups()

    print(f"[+] Repo: {repo}")
    print(f"[+] Branch: {branch}")
    print(f"[+] Subfolder: {folder_path}")

    zip_url = f"https://github.com/{user}/{repo}/archive/refs/heads/{branch}.zip"

    print("[+] Downloading ZIP from GitHub...")
    r = requests.get(zip_url, timeout=20)
    r.raise_for_status()

    print("[+] Extracting selected folder...")
    z = zipfile.ZipFile(BytesIO(r.content))

    repo_root = f"{repo}-{branch}"
    extracted = 0

    for file in z.namelist():
        if file.startswith(f"{repo_root}/{folder_path}"):
            relative_path = file[len(f"{repo_root}/{folder_path}/"):]
            if relative_path:
                target_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with z.open(file) as source, open(target_path, "wb") as target:
                    target.write(source.read())
                extracted += 1

    print(f"[✔] {extracted} files extracted.")
    print(f"[→] Saved to: {os.path.abspath(output_dir)}")

def main():
    parser = argparse.ArgumentParser(description="Clone a specific folder from a GitHub repo.")
    parser.add_argument("url", help="GitHub folder URL")
    parser.add_argument("output", help="Output directory")

    args = parser.parse_args()
    clone_github_folder(args.url, args.output)

if __name__ == "__main__":
    main()
