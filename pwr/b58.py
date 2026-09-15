from typing import Union

# Bitcoinで標準的に使われる Base58 アルファベット (0, O, I, l などの誤認しやすい文字を除外)
B58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def b58e(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """Base58 エンコード処理
    
    :param data: エンコード対象 (str または bytes)
    :param encoding: str入力時の文字コード
    :return: Base58エンコード済み文字列
    """
    if isinstance(data, str):
        data_bytes = data.encode(encoding)
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    if not data_bytes:
        return ""

    # 先頭のヌルバイト (\x00) の個数をカウント (Base58の'1'に対応)
    zero_count = 0
    for b in data_bytes:
        if b == 0:
            zero_count += 1
        else:
            break

    # バイト列を数値に変換してBase58計算
    num = int.from_bytes(data_bytes, "big")
    res = []
    while num > 0:
        num, mod = divmod(num, 58)
        res.append(B58_ALPHABET[mod])

    # 先頭ゼロ分の '1' を復元して結合
    return "1" * zero_count + "".join(reversed(res))


def b58d(
    data: Union[str, bytes], 
    decode: bool = False, 
    encoding: str = "utf-8", 
    errors: str = "ignore"
) -> Union[bytes, str]:
    """Base58 デコード処理 (デフォルト: bytes)
    
    :param data: デコード対象 (str または bytes)
    :param decode: True の場合、結果を文字列(str)で返す
    :param encoding: decode=True 時の文字コード
    :param errors: デコード失敗時の挙動
    :return: デコード後の bytes または str
    """
    if isinstance(data, str):
        clean_data = data.strip().replace("\n", "").replace(" ", "")
    elif isinstance(data, (bytes, bytearray)):
        clean_data = data.decode("ascii").strip().replace("\n", "").replace(" ", "")
    else:
        raise TypeError("Input must be str or bytes")

    if not clean_data:
        return b"" if not decode else ""

    # 先頭の '1' の個数をカウント (\x00 に戻す)
    zero_count = 0
    for c in clean_data:
        if c == "1":
            zero_count += 1
        else:
            break

    # 数値へ復元
    num = 0
    for c in clean_data:
        if c not in B58_ALPHABET:
            raise ValueError(f"Invalid Base58 character: '{c}'")
        num = num * 58 + B58_ALPHABET.index(c)

    # 数値をバイト列に変換
    if num == 0:
        res_bytes = b""
    else:
        # 必要なバイト長を計算
        length = (num.bit_length() + 7) // 8
        res_bytes = num.to_bytes(length, "big")

    res = (b"\x00" * zero_count) + res_bytes

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
