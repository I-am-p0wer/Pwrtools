# powertools/rot13.py
def rot13(data):
    """ROT13 (文字列 / bytes 対応)"""
    if isinstance(data, str):
        res = []
        for c in data:
            if 'a' <= c <= 'z':
                res.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= c <= 'Z':
                res.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
            else:
                res.append(c)
        return "".join(res)
    elif isinstance(data, (bytes, bytearray)):
        res = bytearray()
        for b in data:
            if ord('a') <= b <= ord('z'):
                res.append((b - ord('a') + 13) % 26 + ord('a'))
            elif ord('A') <= b <= ord('Z'):
                res.append((b - ord('A') + 13) % 26 + ord('A'))
            else:
                res.append(b)
        return bytes(res)
    else:
        raise TypeError("Input must be str or bytes")
