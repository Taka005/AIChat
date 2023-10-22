import markovify
import MeCab
import json
import sys
import random

def getNouns(text):
    tagger = MeCab.Tagger("-Ochasen")
    words = tagger.parse(text).split("\n")
    return [word.split("\t")[0] for word in words if "名詞" in word]

if len(sys.argv) > 1:
    nouns = getNouns(sys.argv[1])
    start = random.choice(nouns)
    
    isStartText = True
else:
    isStartText = False

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)

tagger = MeCab.Tagger("-Owakati")
data = "\n".join([tagger.parse(sentence) for sentence in data])
model = markovify.NewlineText(data)

for _ in range(20):
    if isStartText:
        response = model.make_sentence_with_start(beginning=start,tries=100)
    else:
        response = model.make_short_sentence(100,30,tries=100)

    if response is not None:
        response = response.replace(" ","")
    else:
        response = "生成できませんでした"

    print(response)