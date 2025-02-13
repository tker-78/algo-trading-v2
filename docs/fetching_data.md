# fetching candle data and storing it

## 機能
データ処理において下記の機能を有する。

- ローソク足関連
  - 定義したモデルに応じてテーブルを作成する
  - csv形式のデータを読み込み、データベースに保存する 
  - (optional)最新のデータをwebから取得してデータベースを更新する

## 実装メモ


### DB設計

- trade用: algo2_trade
- backtest用: algo2_backtest

```bash
$ brew services list
$ brew services start postgresql@14
$ psql postgres;
#=> CREATE DATABASE algo2_trade
#=> CREATE DATABASE algo2_backtest
```


```bash
# ファイルからデータベース定義を読み込み
$ psql -d algo2_backtest -f schema_def.sql -v ON_ERROR_STOP=1
```

### データベースとの接続
下記でpostgresqlに接続できれば、接続情報が正しいことが確認できる。
```bash
# データベースとの接続確認
$ psql "postgresql://takuyakinoshita:@localhost:5432/algo2_backtest" 
```


### テーブルの作成

~~`schema_def.sql`を実行する。~~

`base.py`に定義している`init_db()`を実行することでテーブルが作成される。
`__init__.py`で実行を指示しているので、modelsモジュールが読み込まれる際に実行される。


### データのインポート
PyCharmの機能を使ってデータベースに流し込む。
csvをディレクトリに保存して、右クリック > 「データベースにインポート」を選択。


