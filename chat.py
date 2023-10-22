import markovify
import MeCab
import json
import sys
import random

def getNouns(text):
    tagger = MeCab.Tagger("-Ochasen")
    words = tagger.parse(text).split("\n")
    nouns = [word.split("\t")[0] for word in words if "名詞" in word]
    if not nouns:
        nouns = random.choice(words)
    return nouns

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)

tagger = MeCab.Tagger("-Owakati")
data = "\n".join([tagger.parse(sentence) for sentence in data])
model = markovify.NewlineText(data)

while True:
    try:
        user_input = input("ユーザー: ")
        nouns = getNouns(user_input)
        start = random.choice(nouns)

        text = model.make_sentence_with_start(beginning=start,tries=100).replace(" ","")
    except:
        text = "生成できませんでした"

    print(f"ボット: {text}")