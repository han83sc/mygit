# Using Python to get JSON from http and save as json file
# by seaniwei

import requests
import json
data = requests.get(url="https://quality.data.gov.tw/dq_download_json.php?nid=127631&md5_url=5582f416b5f008d6faf08ed4c9dfd7aa")
with open("music.json","w",encoding="utf-8") as myFile:
    json.dump(data.json(), myFile,ensure_ascii=False)
myFile.close()
