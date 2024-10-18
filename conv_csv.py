import customtkinter as ctk
from tkinter import messagebox  # ダイアログ表示に使用
import pandas as pd
import csv
import tempfile
import os
import requests
import sys

# アップデート機能の実装
GITHUB_API_URL = "https://api.github.com/repos/takumi-saka-mo/windows_conv_csv/releases/latest"
DOWNLOAD_URL = "https://github.com/takumi-saka-mo/windows_conv_csv/releases/latest/download/conv_csv.exe"

def check_for_update(current_version):
    try:
        response = requests.get(GITHUB_API_URL)
        latest_release = response.json()
        latest_version = latest_release['tag_name']  # リリースのバージョンを取得

        if latest_version > current_version:
            return True
        else:
            return False
    except Exception as e:
        print(f"アップデートチェックに失敗しました: {e}")
        return False

def download_latest_version():
    try:
        response = requests.get(DOWNLOAD_URL, stream=True)
        with open("conv_csv_new.exe", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        os.replace("conv_csv_new.exe", "conv_csv.exe")
        messagebox.showinfo("更新完了", "アプリケーションが更新されました。")
        os.execv(sys.executable, ['python'] + sys.argv)
    except Exception as e:
        messagebox.showerror("エラー", f"アップデートに失敗しました: {e}")

def prompt_update():
    CURRENT_VERSION = "v1.0"
    if check_for_update(CURRENT_VERSION):
        if messagebox.askyesno("更新確認", "新しいバージョンがあります。更新しますか？"):
            download_latest_version()

# GUI部分
FONT_TITLE = ("Calibri", 16, "bold")
FONT_LABEL = ("Calibri", 12)
FONT_BUTTON = ("Calibri", 12)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("convert csv-file")
root.geometry("500x300")

prompt_update()  # 起動時にアップデートチェック

# Globalとして定義
csv_file_path = ""
utf8_file_path = ""

# ファイルの選択
def select_file():
    global csv_file_path
    csv_file_path = ctk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        file_label.configure(text=f"選択されたファイル: {csv_file_path.split('/')[-1]}")

# CSVをUTF-8に変換後, 一時ファイルに保存する処理
def preprocess_csv_to_tempfile(input_file_path, original_encoding='shift-jis'):
    try:
        # 一時ファイル(utf-8)を作成 ⇒ クリップボードにコピーが完了次第削除する作動
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode='w', encoding='utf-8', newline='')
        utf8_file_path = temp_file.name
        
        with open(input_file_path, 'r', encoding=original_encoding, newline='') as infile, temp_file:
            reader = csv.reader(infile)
            writer = csv.writer(temp_file)
            
            for row in reader:
                # フィールド数が異なる場合の処理
                if len(row) < 34:
                    row.extend([''] * (34 - len(row)))  # フィールドが足りない場合, 空白を追加
                elif len(row) > 34:
                    row = row[:34]  # フィールドが多い場合, 余分な部分を削除
                
                writer.writerow(row)
        
        return utf8_file_path
    except Exception as e:
        status_label.configure(text=f"Error : エンコーディング変換エラー \n{str(e)}", text_color="red")
        return None

# データをクリップボードにコピーする処理
def copy_to_clipboard(copy_type):
    global csv_file_path
    if not csv_file_path:
        status_label.configure(text="ファイルを選択してください", text_color="red")
        return
    
    # CSVをUTF-8に変換して一時ファイルに保存
    utf8_file_path = preprocess_csv_to_tempfile(csv_file_path)
    
    if not utf8_file_path:
        return

    try:
        # UTF-8で保存された一時ファイルを読み込み
        df = pd.read_csv(utf8_file_path)

        if copy_type == "FOODS":
            # 範囲を抽出して行列を入れ替える操作
            sub_df = df.iloc[1:4, 2:33]  # 月末指定のスクリプトを差し込む必要
            transposed_df = sub_df.T
            # データをクリップボードにコピー
            transposed_df.to_clipboard(index=False, header=False)
            status_label.configure(text="食品・酒類 データをクリップボードへコピーしました.", text_color="green")

        elif copy_type == "MATERIALS":
            # 資材系データのコピー
            sub_df2 = df.iloc[4:5, 2:33]  # 月末指定のスクリプトを差し込む必要
            transposed_df2 = sub_df2.T
            # データをクリップボードにコピー
            transposed_df2.to_clipboard(index=False, header=False)
            status_label.configure(text="資材系 データをクリップボードへコピーしました.", text_color="green")

    except Exception as e:
        status_label.configure(text=f"クリップボードへのコピー中にエラーが発生しました: \n{str(e)}", text_color="red")
    finally:
        # 処理後に一時ファイルを削除
        if utf8_file_path and os.path.exists(utf8_file_path):
            os.remove(utf8_file_path)

# 以下レイアウト

# ファイル選択ボタン
select_button = ctk.CTkButton(root, text="csvファイルを選択", command=select_file, font=FONT_BUTTON)
select_button.pack(pady=40)

# 3社のデータをクリップボードにコピーするボタン
copy_button_3sha = ctk.CTkButton(root, text="クリップボードにコピー(食品・酒類)", command=lambda: copy_to_clipboard("FOODS"), font=FONT_BUTTON)
copy_button_3sha.pack(pady=10)

# 資材系データをクリップボードにコピーするボタン
copy_button_shizai = ctk.CTkButton(root, text="   クリップボードにコピー(資材系)   ", command=lambda: copy_to_clipboard("MATERIALS"), font=FONT_BUTTON)
copy_button_shizai.pack(pady=10)

# 選択されたファイル名ラベル
file_label = ctk.CTkLabel(root, text="ファイルが選択されていません", font=FONT_LABEL)
file_label.pack(pady=10)

# 処理結果ラベル
status_label = ctk.CTkLabel(root, text="", font=FONT_LABEL)
status_label.pack(pady=10)

root.mainloop()