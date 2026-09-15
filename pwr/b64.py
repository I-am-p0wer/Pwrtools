import base64
from typing import Union

def b64e(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """Base64 エンコード処理"""
    if isinstance(data, str):
        data_bytes = data.encode(encoding)
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    return base64.b64encode(data_bytes).decode("ascii")


def b64d(
    data: Union[str, bytes], 
    decode: bool = False, 
    encoding: str = "utf-8", 
    errors: str = "ignore"
) -> Union[bytes, str]:
    """Base64 デコード処理 (デフォルト: bytes)"""
    if isinstance(data, str):
        clean_data = data.strip().replace("\n", "").replace(" ", "")
        data_bytes = clean_data.encode("ascii")
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    missing_padding = len(data_bytes) % 4
    if missing_padding:
        data_bytes += b"=" * (4 - missing_padding)

    res = base64.b64decode(data_bytes)

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
