import base64
from typing import Union

def b85e(data: Union[str, bytes], ascii85: bool = False, encoding: str = "utf-8") -> str:
    """Base85 / Ascii85 エンコード処理"""
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
    """Base85 / Ascii85 デコード処理 (デリミタ自動除去機能付き)"""
    if isinstance(data, str):
        clean_data = data.strip().replace("\n", "").replace(" ", "")
        # Ascii85 のデリミタ <~ と ~> を自動除去
        if clean_data.startswith("<~"):
            clean_data = clean_data[2:]
            ascii85 = True
        if clean_data.endswith("~>"):
            clean_data = clean_data[:-2]
            ascii85 = True
        data_bytes = clean_data.encode("ascii")
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
        if data_bytes.startswith(b"<~"):
            data_bytes = data_bytes[2:]
            ascii85 = True
        if data_bytes.endswith(b"~>"):
            data_bytes = data_bytes[:-2]
            ascii85 = True
    else:
        raise TypeError("Input must be str or bytes")

    if ascii85:
        res = base64.a85decode(data_bytes)
    else:
        res = base64.b85decode(data_bytes)

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
