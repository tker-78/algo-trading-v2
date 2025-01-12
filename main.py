import argparse

def backtest():
    print("executing backtest")

def trade():
    """
    backtest()とtrade()は基本的には同じ機能を使う。
    ただし、問い合わせ先のデータベースを切り分ける。
    trade()は本番環境,
    backtest()は検証環境に接続する。
    """
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



if __name__ == '__main__':
    main()

