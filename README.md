# csv2exo

KoeMill の `.csv` 出力したものを `.exo` に変換するもの

`main.bat` に `.csv` をD&Dして `framerate:` を入力すると、`.csv` があるディレクトリに `str.exo` が生成されます

## require

[PSDToolKit](https://github.com/oov/aviutl_psdtoolkit)の字幕準備を使用してます\
非導入環境の場合は、`main.py` の `enable_PTK = True` を `enable_PTK = False` に書き換えてください
> main.py L33~35 を書き換えるとテンプレートを変更できます
