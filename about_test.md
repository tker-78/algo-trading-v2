# Pytestに関するTips

このレポジトリではPytestを用いて自動テストを行なっている。

プログラムを実装する過程で得た知見をここに残しておく。

## caplog
`caplog`は、テスト中に生成されたログメッセージをキャプチャして、アサーションに利用できる。

```python
import logging

def test_sample(caplog):
    with caplog.at_level(logging.INFO):
        some_method()
        assert "expected message" in caplog.text
```


