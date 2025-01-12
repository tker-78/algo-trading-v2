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

```sql

```














