import json
import re

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)

def is_valid_item(item):
    return not re.search(r'@everyone|@here',item) and not re.search(r'<(a)?:\w+:\d+>',item) and not re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',item) and item != ""

data = list(filter(is_valid_item,data))

with open("data.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

print("処理が完了しました")
