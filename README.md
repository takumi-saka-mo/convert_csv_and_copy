# convert_csv_and_copy

## Summary

convert_csv_and_copy は、CSVファイルを選択し、特定の範囲をクリップボードに転置＆コピーするアプリケーション.<br>
Microsoft Office Onlineでの機能制限に対応するために開発. GitHubを使用した自動アップデート機能も実装.<br>
**exeファイルのダウンロードは下記のリンクから**
<br>
https://github.com/takumi-saka-mo/convert_csv_and_copy/releases/latest/download/conv_csv.exe


## Option

- CSVファイルの選択と表示
- UTF-8へのエンコーディング変換
- 特定の範囲の行・列のデータをクリップボードにコピー
- GitHubリリースから自動的にアップデート

## Environment

- Python 3.6以降
- 以下のPythonパッケージが必要
- customtkinter
- pandas
- requests

必要なパッケージは、以下のコマンドでインストールできます。
```bash
pip install customtkinter pandas requests
```

## Install
1. 本リポジトリをクローン
```bash
git clone https://github.com/takumi-saka-mo/convert_csv_and_copy.git
cd convert_csv_and_copy
```

2. 必要なPythonパッケージをインストール
```bash
pip install -r requirements.txt
```
3. アプリケーションを起動
```bash
python conv_csv.py
```




## Usage

1. CSVファイルの選択

起動後、「csvファイルを選択」ボタンをクリックして、CSVファイルを選択してください。

2. データのコピー

選択したCSVファイルの特定範囲をクリップボードにコピーできます。以下のボタンを使用します：

- クリップボードにコピー(食品・酒類)：食品・酒類データ(元データ 3行 ⇒ 貼り付け字3列)をクリップボードにコピーします。
- クリップボードにコピー(資材系)：資材系データ(元データ 1行29〜31列 ⇒ 29〜31行1列)をクリップボードにコピーします。

3. アップデート機能

**アプリケーション起動時に、GitHub上のリリースから新しいバージョンがあるかをチェックする機能**
GitHub上のリリース情報を利用した自動アップデート機能が搭載されています。アプリケーションが起動する際、GitHub APIを通じて最新バージョンを確認し、必要に応じて更新を行います。

# How to auto-Update

1.	conv_csv.py 実行時に、GitHub APIを介して最新バージョンを確認.
2.	新しいバージョンがある場合、ユーザーに更新の確認.
3.	ユーザーが更新を選択した場合、最新のバイナリ（conv_csv.exe）をGitHubリリースページからダウンロードし, 自動置き換え.
4.	アプリケーションを自動的に再起動.


## License

このプロジェクトはMITライセンスの下で公開.


### 僕へ
GitのデフォルトのHTTPバッファサイズを増やして、Pushを処理しやすくするなるらしい...
```bash
git config http.postBuffer 524288000
```
↓
```bash
git push origin main
```

