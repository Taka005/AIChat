import json
import re

# JSONファイルを読み込む
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 正規表現パターン
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
discord_emoji_pattern = r'<(a)?:\w+:\d+>'

# 要素のフィルタリング
def is_valid_item(item):
    return not re.search(url_pattern, item) and not re.search(discord_emoji_pattern, item) and item != ""

filtered_data = list(filter(is_valid_item, data))

# 結果を元のファイルに上書き保存
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=2)

print("処理が完了しました。data.jsonが上書き保存されました。")
