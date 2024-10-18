# convert_csv_and_copy

## 概要

convert_csv_and_copy は、CSVファイルを選択し、特定の範囲をクリップボードにコピーするアプリケーションです。さらに、GitHubを使用した自動アップデート機能を備えています。このアプリケーションは、PythonとCustomTkinterを使用してGUIを提供します。
**exeファイルのダウンロードは下記のリンクから**
https://github.com/takumi-saka-mo/convert_csv_and_copy/releases/latest/download/conv_csv.exe


## 機能

- CSVファイルの選択と表示
- UTF-8へのエンコーディング変換
- 特定の範囲の行・列のデータをクリップボードにコピー
- GitHubリリースから自動的にアップデート

## 前提条件

- Python 3.6以降
- 以下のPythonパッケージが必要です。
- customtkinter
- pandas
- requests

必要なパッケージは、以下のコマンドでインストールできます。
```bash
pip install customtkinter pandas requests
```

## Install
1. このリポジトリをクローン
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



＃＃
## Usage

1. CSVファイルの選択

起動後、「csvファイルを選択」ボタンをクリックして、CSVファイルを選択してください。

2. データのコピー

選択したCSVファイルの特定範囲をクリップボードにコピーできます。以下のボタンを使用します：

- クリップボードにコピー(食品・酒類)：食品・酒類データをクリップボードにコピーします。
- クリップボードにコピー(資材系)：資材系データをクリップボードにコピーします。

3. アップデート機能

アプリケーション起動時に、GitHub上のリリースから新しいバージョンがあるかをチェックします。新しいバージョンがある場合、ダウンロードと自動更新が行われます。

アップデート機能

このアプリケーションには、GitHub上のリリース情報を利用した自動アップデート機能が搭載されています。アプリケーションが起動する際、GitHub APIを通じて最新バージョンを確認し、必要に応じて更新を行います。

# How to auto-Update

1.	conv_csv.py 実行時に、GitHub APIを介して最新バージョンを確認します。
2.	新しいバージョンがある場合、ユーザーに更新の確認を求めます。
3.	ユーザーが更新を選択した場合、最新のバイナリ（conv_csv.exe）をGitHubリリースページからダウンロードし、古いバージョンを置き換えます。
4.	アプリケーションを自動的に再起動します。

開発者向け情報

リリースの作成

アップデート機能を使用するために、GitHubでリリースを作成する必要があります。リリースの作成方法は次の通りです：

1.	GitHubのリポジトリにアクセスし、「Releases」タブに移動します。
2.	「Draft a new release」をクリックし、以下を設定します：
	-	タグ名: v1.0（などのバージョン番号）
	-	リリースノート: 任意でバージョンごとの変更点などを記載します。
	-	バイナリファイルの添付: conv_csv.exe をアップロードします。
3.	「Publish release」をクリックしてリリースを公開します。

## License

このプロジェクトはMITライセンスの下で公開.

