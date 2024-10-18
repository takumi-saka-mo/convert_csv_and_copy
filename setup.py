from setuptools import setup

APP = ['conv_csv.py']  # 実行するPythonスクリプト
OPTIONS = {
    'argv_emulation': True,  # Windowsでは不要
    'includes': ['customtkinter', 'pandas'],  # 使用しているパッケージをリストアップ
}

setup(
    app=APP,
    options={'py2app': OPTIONS},  # ここは `py2app` の場合。WindowsではPyInstallerを使用
    setup_requires=['py2app'],  # Windowsでは不要
)