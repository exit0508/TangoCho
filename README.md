# TangoCho
Python3で作成した単語帳を作成する簡易的なプログラムになります.  
あらかじめCSVファイルで英単語のリストを作成し，それを読み込み，Weblioの主な意味を抽出し，異なるファイルに英単語とスクレイピングした意味を合わせて書き出します．  
そのファイルを使えばQuizletに単語と意味をインポートできるかと思います．以下が具体的な使い方です．  

1. インポートしたい英単語リストをCSVファイルで用意する  
1. TangoChoのimport_words.py内のインポートとエクスポートするファイル場所を書き換える  
1. プログラム実行後，英単語とWeblioから抽出した意味を併せてエクスポートしたファイルができます  

#参考サイト
- [webスクレイピングで英単語の和訳を取得する](https://kazzstorage.com/scraping-spell/)
- [【Python】初心者が Pythonで英単語帳を作ってみた〜検索・保存編〜](https://py-memo.com/python/english-wordbook-part1/)
