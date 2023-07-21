import csv
from pathlib import Path

# CSVファイルが入っているディレクトリ名を指定
csv_file = Path("GeoCSVs").rglob("*.csv")

header_saved = False

# merged.csvファイルを作成
# 名前を変更したい場合は、"merged.csv"の部分を変更する

with open("merged.csv", "w", newline="") as fout:
    # csvwriterオブジェクトを作成
    writer = csv.writer(fout)
    # ディレクトリの中に入っているcsvファイルを頭から１つずつ読む
    # この時、ファイル名を昇順にソートする
    for filename in sorted(csv_file):
        print(filename)
        # csvファイルを開く
        with open(filename, newline="") as fin:
            # csvファイルを読み込む
            reader = csv.reader(fin)
            # ヘッダーをスキップする
            header = next(reader)
            # ヘッダーがまだ書き込まれていなければ、書き込む
            if not header_saved:
                writer.writerow(header)
                header_saved = True
            # １行ずつ新しいmerged.csvファイルに書き込む
            for row in reader:
                writer.writerow(row)
