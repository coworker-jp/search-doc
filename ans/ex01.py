from typing import List, Dict, Set

from janome.tokenizer import Tokenizer


def tokenize(document: str) -> List[str]:
    """形態素解析を行う
    形態素解析を行い、品詞が名詞以外のものは除去する
    """
    tokens = []
    tokenizer = Tokenizer()
    for token in tokenizer.tokenize(document):
        if token.part_of_speech.startswith("名詞"):
            tokens.append(token.surface)
    return tokens


def make_index(documents: Dict[str, str]) -> Dict[str, list]:
    """転置インデックスを作成する関数
    Key:単語、Value:文書番号のリストを作成する
    """
    index = {}
    for document_id, document_text in documents.items():
        tokens = tokenize(document_text)
        for token in tokens:
            if token not in index.keys():
                index[token] = []
            index[token].append(document_id)
    return index


def search(index: Dict[str, str], query: str) -> Set[str]:
    """転置インデックスを利用して、検索ワードが含まれる文書IDの集合を返す"""
    document_ids = set()
    tokens = tokenize(query)
    for token in tokens:
        if token in index:
            result = index[token]
            document_ids.update(result)
    return document_ids

