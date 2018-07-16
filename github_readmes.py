import httplib
import json
import time
from pprint import pprint

# final results: 1915 / 1949 = 98%

REQUEST_DELAY = 2 # 10s
README_DIR = "READMES"
GITHUB_HOST = "raw.githubusercontent.com"
BRANCH = "master"
README_FILES = [ "README.md", "readme.md", "Readme.md", "README", "README.rst", "README.markdown", "readme.markdown", "README.mdown", "README.txt", "README.textfile" ]

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPSConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return 0

def get_readme(host, path="/"):
    try:
        conn = httplib.HTTPSConnection(host)
        conn.request("GET", path)
        resp = conn.getresponse()
        if resp.status == 200:
            return resp.read()
        return None
    except StandardError:
        return None

with open('repos.json') as f:
    repos = json.load(f)

for idx, repo in enumerate(repos):
    username, project = repo["title"].split('/')

    for filename in README_FILES:

        PATH = "/%s/%s/%s/%s" % (username, project, BRANCH, filename)
        status_code = get_status_code(GITHUB_HOST, PATH)

        print("<%s> (%d)" % (GITHUB_HOST + PATH, status_code))

        if status_code == 200:
            readme_body = get_readme(GITHUB_HOST, PATH)
            if len(readme_body) > 0:

                extension = ""
                name = filename
                if "." in filename:
                    name, extension = filename.split('.')

                FILENAME_OUT = "./%s/%s.%s.%s" % (README_DIR, username, project, extension)
                print("Writing " + FILENAME_OUT)

                with open(FILENAME_OUT, "w") as fo:
                    fo.write(readme_body)
                    fo.close()

                time.sleep(REQUEST_DELAY)
                break

print("Wrote %d READMEs" % len(repos))