import base64
from typing import Union

def b85e(data: Union[str, bytes], ascii85: bool = False, encoding: str = "utf-8") -> str:
    """Base85 エンコード処理
    
    :param data: エンコード対象 (str または bytes)
    :param ascii85: True の場合、Ascii85 (Adobe variant) を使用
    :param encoding: str入力時の文字コード
    :return: エンコード済み文字列
    """
    if isinstance(data, str):
        data_bytes = data.encode(encoding)
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    if ascii85:
        return base64.a85encode(data_bytes).decode("ascii")
    return base64.b85encode(data_bytes).decode("ascii")


def b85d(
    data: Union[str, bytes], 
    ascii85: bool = False,
    decode: bool = False, 
    encoding: str = "utf-8", 
    errors: str = "ignore"
) -> Union[bytes, str]:
    """Base85 デコード処理 (デフォルト: bytes)
    
    :param data: デコード対象 (str または bytes)
    :param ascii85: True の場合、Ascii85 (Adobe variant) としてデコード
    :param decode: True の場合、結果を文字列(str)で返す
    :param encoding: decode=True 時の文字コード
    :param errors: デコード失敗時の挙動
    :return: デコード後の bytes または str
    """
    if isinstance(data, str):
        clean_data = data.strip().replace("\n", "").replace(" ", "")
        data_bytes = clean_data.encode("ascii")
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    if ascii85:
        res = base64.a85decode(data_bytes)
    else:
        res = base64.b85decode(data_bytes)

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
