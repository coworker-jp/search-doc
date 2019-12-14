from ex01 import tokenize, make_index, search


def test_tokenize():
    assert tokenize(document="チョムスキーとは、アメリカの学者である") == ["チョムスキー", "アメリカ", "学者"]
    assert tokenize(document="アインシュタインとは、ドイツの学者である") == ["アインシュタイン", "ドイツ", "学者"]
    assert tokenize(document="ベルとは、スコットランドの発明家である。") == ["ベル", "スコットランド", "発明", "家"]


def test_make_index():
    documents = {
        "doc01": "チョムスキーとは、アメリカの学者である",
        "doc02": "アインシュタインとは、ドイツの学者である",
        "doc03": "ベルとは、スコットランドの発明家である。",
    }
    assert make_index(documents) == {
        "チョムスキー": ["doc01"],
        "アメリカ": ["doc01"],
        "学者": ["doc01", "doc02"],
        "アインシュタイン": ["doc02"],
        "ドイツ": ["doc02"],
        "ベル": ["doc03"],
        "スコットランド": ["doc03"],
        "発明": ["doc03"],
        "家": ["doc03"]
    }


def test_search():
    index = make_index({
        "doc01": "チョムスキーとは、アメリカの学者である",
        "doc02": "アインシュタインとは、ドイツの学者である",
        "doc03": "ベルとは、スコットランドの発明家である。",
    })
    assert search(index, query="チョムスキーって誰だっけ") == {"doc01"}
    assert search(index, query="学者") == {"doc01", "doc02"}
    assert search(index, query="アメリカとスコットランド") == {"doc01", "doc03"}
    assert search(index, query="アインシュタインはドイツ人") == {"doc02"}
