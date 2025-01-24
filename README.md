# algo-trading-v2

- 設計を見直して変更に強くする
- 単体テストを実装する
- CLIでトレード条件を指定できるようにする
  - `argparse`モジュールを使う
- 同じプログラム内でバックテストを実行できる


### argparseの使い方

```bash
# backtestを実行
$ python3 main.py --backtest

# トレードを実行
$ python3 main.py --trade

```

下記の実装で実現できる.
`add_mutually_exclusive_group()`は引数に`action="store_true"`を指定する必要がある。
```python
import argparse
def backtest():
    print("executing backtest")

def trade():
    print("executing trade")

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--backtest", action="store_true")
    group.add_argument("--trade", action="store_true")
    args = parser.parse_args()
    if args.backtest:
        backtest()
    elif args.trade:
        trade()
    else:
        print("please indicate correct argument.")
```


### backtest()で実行すること
- 過去のデータを用いて、トレードシミュレーションを行う。
- 検証環境データベースに接続する
- データベースに最新の為替データを反映する
- シミュレーション結果の収益を表示する
- シミュレーションの条件と収益をデータベースに保存する。

### trade()で実行すること
- GMOコインのAPI経由でトレードを行う
  - トレードは成行注文のみ
- トレードシミュレーションと同じメソッドを使用して、注文を出す
- トレードの状況をwebサーバーから配信して、ブラウザ経由で確認できるようにする

## stream.py
トレードおよびバックテストの実行は`main.py`が受け持つが、
tickデータの受信とデータベースへの格納は、`stream.py`が受け持つ。

- 取引時間外のデータは自動削除する
- トレードに使用する指標(SMAなど)をリアルタイムで演算して、別データベースに格納する


## トレードアルゴリズムの作り込み
前回のプログラムを、見通しの良い構成に変更する。

ローソク足情報をデータベースに保存し、そこから、分析に必要なデータを`dfCandle`が取り出す。  
dfCandleでは分析は行わず、分析は`Conductor`が行う。  
つまり、分析に必要な条件(価格、数量、モメンタムなど)はConductorが受け持つ。  
tradeとbacktestの切り替えもConductorが行うため、データベースへの接続情報も与える。

大体こんな感じになる
```python
class DBConnection(): pass
class Conductor(): 
  def __init__(self, trade=False):
    if trade:
      self.db_connection = "trade_db_connection"
    else:
      self.db_connection = "backtest_db_connection"
    
cond = Conductor(trade=True)
```


## DB設計

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

## Candleクラス

Candleクラスは、tickerから値を取得してデータベースに格納する機能を持つ。

必要なメソッドは下記の通り。

- candleを作る。cls.create()
- candleを更新する。self.update()
- candleを削除する。self.delete()
- candleを取り出す。
  - cls.get_candles_by_limit()
  - cls.get_candles_between()


## APIClient

APIは、GMO, OANDAのどちらも使えるようにインターフェースを共通化する。
private, publicそれぞれで、下記のメソッドを実装する。


### public
- get_spread()



### private
#### GET
- authorization(): 認証
- get_balance(): 資産残高を取得
- get_open_positions(): 現在の建玉を取得
- get_execution(): 約定情報を取得
- get_assets(): 現在の資産を取得
- get_latest_executions(): 最新の約定を取得

#### POST
- place_buy_order(): 買い注文
- place_sell_order(): 売り注文
- close_order(): 建玉を指定して決済
- close_out(): 全ての建玉を決済(ロスカット用)


### Stream
- Ticker class: streamから値を読み込むオブジェクトを生成













