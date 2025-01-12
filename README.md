# algo-trading-v2

- 設計を見直して変更に強くする
- 単体テストを実装する
- CLIでトレード条件を指定できるようにする
  - `argparse`モジュールを使う
- 同じプログラム内でバックテストを実行できる


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


