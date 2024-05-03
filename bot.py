import discord
import markovify
import MeCab
import json
import sys
import random

def getStartText(text):
    tagger = MeCab.Tagger("-Ochasen")
    words = tagger.parse(text).split("\n")[:-2]
    nouns = [word.split("\t")[0] for word in words if "名詞" in word]
    if nouns:
        return random.choice(nouns)
    else:
        return random.choice(words).split("\t")[0]

def getText(input):
    tries = 0
    text = None
    while tries < 5:
        start = getStartText(user_input)

        try:
            text = model.make_sentence_with_start(beginning=start,tries=100).replace(" ", "")
            break
        except:
            tries += 1

    if text is None:
        text = "生成できませんでした"

    return text

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)

print(f"{len(data)}行をロードしました")

tagger = MeCab.Tagger("-Owakati")
data = "\n".join([tagger.parse(sentence) for sentence in data])
model = markovify.NewlineText(data)

client = discord.Client()

@client.event
async def on_ready():
    print("ログインしました")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == "1235791172656693268":
        await message.channel.send(content=getText(message.content),allowed_mentions=discord.AllowedMentions.none())

client.run("")