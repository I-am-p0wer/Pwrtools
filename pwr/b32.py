import base64
from typing import Union

def b32e(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """Base32 エンコード処理
    
    :param data: エンコード対象 (str または bytes)
    :param encoding: str入力時の文字コード
    :return: Base32エンコード済み文字列
    """
    if isinstance(data, str):
        data_bytes = data.encode(encoding)
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    return base64.b32encode(data_bytes).decode("ascii")


def b32d(
    data: Union[str, bytes], 
    decode: bool = False, 
    encoding: str = "utf-8", 
    errors: str = "ignore"
) -> Union[bytes, str]:
    """Base32 デコード処理 (デフォルト: bytes)
    
    :param data: デコード対象 (str または bytes)
    :param decode: True の場合、結果を文字列(str)で返す
    :param encoding: decode=True 時の文字コード
    :param errors: デコード失敗時の挙動
    :return: デコード後の bytes または str
    """
    if isinstance(data, str):
        clean_data = data.strip().replace("\n", "").replace(" ", "").upper()
        data_bytes = clean_data.encode("ascii")
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data).upper()
    else:
        raise TypeError("Input must be str or bytes")

    # パディング (=) の自動補完 (Base32は8文字単位)
    missing_padding = len(data_bytes) % 8
    if missing_padding:
        data_bytes += b"=" * (8 - missing_padding)

    res = base64.b32decode(data_bytes)

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
