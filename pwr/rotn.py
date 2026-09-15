from typing import Union

def rot_n(data: Union[str, bytes], n: int) -> Union[str, bytes]:
    """任意のシフト数で ROT 変換を実行
    
    :param data: 変換対象 (str または bytes)
    :param n: シフト数 (マイナス値や26以上の数値も自動調整)
    :return: 変換後のデータ (入力と同じ型)
    """
    n = n % 26
    if isinstance(data, str):
        res = []
        for c in data:
            if 'a' <= c <= 'z':
                res.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))
            elif 'A' <= c <= 'Z':
                res.append(chr((ord(c) - ord('A') + n) % 26 + ord('A')))
            else:
                res.append(c)
        return "".join(res)
    elif isinstance(data, (bytes, bytearray)):
        res = bytearray()
        for b in data:
            if ord('a') <= b <= ord('z'):
                res.append((b - ord('a') + n) % 26 + ord('a'))
            elif ord('A') <= b <= ord('Z'):
                res.append((b - ord('A') + n) % 26 + ord('A'))
            else:
                res.append(b)
        return bytes(res)
    else:
        raise TypeError("Input must be str or bytes")


def rot13(data: Union[str, bytes]) -> Union[str, bytes]:
    """ROT13 処理 (rot_n(data, 13) のショートカット)"""
    return rot_n(data, 13)


def rot_brute(data: Union[str, bytes], known_str: str = "") -> list:
    """ROT1〜25 の総当たり全探索"""
    results = []
    for i in range(1, 26):
        res = rot_n(data, i)
        if known_str:
            if isinstance(res, str) and known_str not in res:
                continue
            elif isinstance(res, (bytes, bytearray)) and known_str.encode("utf-8") not in res:
                continue
        results.append((i, res))
    return results
