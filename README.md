# CALINT データをくっつけるスクリプト

## 操作方法

- PC 上に、任意のディレクトリを作り、そこに git clone する。
  -
- コマンドラインで、そのディレクトリまで移動する
  - `cd 作ったディレクトリ`
- GeoCSVs フォルダの中に結合したい CSV ファイルを入れる
- そのディレクトリに移動した上で、コマンドラインで `python3 merge_csv_from_calint.py`を実行。
- ディレクトリ内に、マージされた csv ファイルができる。
  - なお、名前を変えたい場合は python ファイル上にやり方を説明しているので、そこを参照すること

## 注意

- CALINT で取得した CSV ファイル以外をフォルダの中に入れないこと
