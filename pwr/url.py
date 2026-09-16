import urllib.parse
from typing import Union

def urle(data: Union[str, bytes], safe: str = "", encoding: str = "utf-8") -> str:
    """URL エンコード処理 (Percent-encoding)
    
    :param data: エンコード対象 (str または bytes)
    :param safe: エンコードから除外する文字 (例: "/:")
    :param encoding: str入力時の文字コード
    :return: URLエンコード済み文字列
    """
    if isinstance(data, str):
        return urllib.parse.quote(data, safe=safe, encoding=encoding)
    elif isinstance(data, (bytes, bytearray)):
        return urllib.parse.quote_from_bytes(bytes(data), safe=safe)
    else:
        raise TypeError("Input must be str or bytes")


def urld(
    data: Union[str, bytes], 
    decode: bool = False, 
    encoding: str = "utf-8", 
    errors: str = "replace"
) -> Union[bytes, str]:
    """URL デコード処理 (デフォルト: bytes)
    
    :param data: デコード対象 (str または bytes)
    :param decode: True の場合、結果を文字列(str)で返す
    :param encoding: decode=True 時の文字コード
    :param errors: デコード失敗時の挙動
    :return: デコード後の bytes または str
    """
    if isinstance(data, str):
        data_str = data.strip()
    elif isinstance(data, (bytes, bytearray)):
        data_str = bytes(data).decode("ascii", errors="ignore").strip()
    else:
        raise TypeError("Input must be str or bytes")

    res_bytes = urllib.parse.unquote_to_bytes(data_str)

    if decode:
        return res_bytes.decode(encoding=encoding, errors=errors)

    return res_bytes
