from typing import List, Dict, Set

from janome.tokenizer import Tokenizer


def tokenize(document: str) -> List[str]:
    """形態素解析を行う
    形態素解析を行い、品詞が名詞以外のものは除去する
    """
    raise NotImplementedError()


def make_index(documents: Dict[str, str]) -> Dict[str, list]:
    """転置インデックスを作成する関数
    Key:単語、Value:文書番号のリストを作成する
    """
    raise NotImplementedError()



def search(index: Dict[str, str], query: str) -> Set[str]:
    """転置インデックスを利用して、検索ワードが含まれる文書IDの集合を返す"""
    raise NotImplementedError()
