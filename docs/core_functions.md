# Implementing core functions

`core`とはトレードに必須の機能。
live-tradeにもbacktestingにも使用する。

- pair
- candle
- dt
- enums
- event
- helpers
- logs
- dispatcher

## pair

トレードペアの名称と、precision(精度)を指定するクラス。

## candle

candleの生成とdatabaseへの格納


## enums

列挙型。
定数管理のために使う。

constants.pyなどを使うよりもこっちの方が名前空間に閉じ込めやすいのでいいかも。


## dt
頻繁に呼び出すdatetime関連のメソッドを定義。

timezoneの設定に混乱したけど下記の処理で解決。

一度tzinfoを与えてあげれば、あとは`self.astimezone(tz.tzutc())`で時差を補正できる。

```python
from datetime import datetime
from dateutil import tz

dt = datetime.now() # datetime.datetime(2025, 2, 15, 20, 1, 55, 816067)
dt = dt.astimezone(tz.tzlocal()) # datetime.datetime(2025, 2, 15, 20, 1, 55, 816067, tzinfo=tzlocal())
dt = dt.astimezone(tz.tzutc()) # datetime.datetime(2025, 2, 15, 11, 1, 55, 816067, tzinfo=tzutc())
```

## event

eventとは、特定の時間に発生するもの。様々な種類があるが、全て時刻をもつ必要がある。

producerは、event-drivenアーキテクチャの重要な役割を持つ。
producerがeventを生成する。













