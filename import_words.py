import requests
from bs4 import BeautifulSoup
import csv
import time

# 単語リストファイルを開く
with open('C:\\Users\\...') as f:
    words_list = f.read().splitlines()

for word in words_list:
    # アクセス先URL
    search_word = "https://ejje.weblio.jp/content/" + word
    # データ取得後＆エンコード設定
    source = requests.get(search_word)
    source.encoding = source.apparent_encoding
    time.sleep(5)
    # BeautifulSoupで抽出
    soup = BeautifulSoup(source.text, "html.parser")
    word_mean = soup.select("td.content-explanation")
    #単語をエクスポートするCSVファイルを作成
    file = 'C:\\Users\...csv'
    f = open(file, 'a', newline='')
    writer = csv.writer(f)

    for idx, txt in enumerate(word_mean):
        meaning = word_mean[idx].text
        time.sleep(5)
        output_list = writer.writerow([word, meaning])
        f.close()
    #スクレイピングと意味の書き出しの進捗状況を表示
    print(str(words_list.index(word)+1) + '/' + str(len(words_list)) +'complete!')

    if len(word_mean) == 0:
        print("meaning is not found")
