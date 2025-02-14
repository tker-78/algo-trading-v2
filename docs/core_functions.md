# Implementing core functions

`core`とはトレードに必須の機能。
live-tradeにもbacktestingにも使用する。

- pair
- candle
- enums
- dispatcher
- event
- helpers
- logs

## pair

トレードペアの名称と、precision(精度)を指定するクラス。

## candle

candleの生成とdatabaseへの格納


## enums

列挙型。
定数管理のために使う。

constants.pyなどを使うよりもこっちの方が名前空間に閉じ込めやすいのでいいかも。







