import markovify
import MeCab
import json
import sys
import random

def get_nouns(text):
    # MeCabを使用して文章から名詞を抽出
    tagger = MeCab.Tagger("-Ochasen")
    words = tagger.parse(text).split('\n')
    nouns = [word.split('\t')[0] for word in words if '名詞' in word]
    return nouns

if len(sys.argv) > 1:
    input_text = sys.argv[1]
    # 入力文から名詞を抽出
    nouns = get_nouns(input_text)
    if nouns:
        # 名詞がある場合、ランダムに選択
        start = random.choice(nouns)
    else:
        # 名詞がない場合、MeCabで分割した文からランダムに単語を選択
        words = input_text.split()
        start = random.choice(words)
    use_make_sentence_with_start = True
else:
    start = ""
    use_make_sentence_with_start = False

# JSONファイルからテキストデータを読み込む
with open('data1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# MeCabを使ってテキストデータを分かち書き
tagger = MeCab.Tagger("-Owakati")
text_data = [tagger.parse(sentence) for sentence in data]

# テキストデータをピリオドで結合
text_data = '\n'.join(text_data)

# Markovifyモデルの作成
text_model = markovify.NewlineText(text_data)

# チャットボットを起動
for _ in range(20):
    if use_make_sentence_with_start:
        response = text_model.make_sentence_with_start(beginning=start,tries=100)
    else:
        response = text_model.make_short_sentence(100, 30, tries=100)
    if response is not None:
        response = response.replace(' ', '')
    else:
        response = "申し訳ありません、応答を生成できませんでした."
    print(response)
