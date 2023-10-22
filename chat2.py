import markovify
import MeCab
import json
import sys
import random

def getStartText(text):
    tagger = MeCab.Tagger("-Ochasen")
    words = tagger.parse(text).split("\n")
    nouns = [word.split("\t")[0] for word in words if "名詞" in word]
    if nouns:
        return random.choice(nouns)
    else:
        return random.choice(words)

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

tagger = MeCab.Tagger("-Owakati")
data = "\n".join([tagger.parse(sentence) for sentence in data])
model = markovify.NewlineText(data)

while True:
    try:
        user_input = input("ユーザー: ")
        tries = 0
        text = None
        while tries < 5:
            start = getStartText(user_input)
            print(f"試行中: {start}")

            try:
                text = model.make_sentence_with_start(beginning=start,tries=100).replace(" ", "")
                break
            except:
                tries += 1

        if text is None:
            text = "生成できませんでした"
    except:
        text = "生成できませんでした"

    print(f"ボット: {text}")
