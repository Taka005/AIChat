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
    user_input = input("ユーザー: ")
    if not user_input:
        text = "入力してください"
    nouns = getNouns(user_input)
    start = random.choice(nouns)
    
    try:
        text = model.make_sentence_with_start(beginning=start,tries=100).replace(" ","")
    except:
        text = "生成できませんでした"

    print(f"BOT: {text}")