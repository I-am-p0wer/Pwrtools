from typing import Union, Optional
from itertools import cycle

def xor(
    data: Union[str, bytes, bytearray], 
    key: Union[str, bytes, bytearray, int],
    decode: bool = False,
    encoding: str = "utf-8",
    errors: str = "ignore"
) -> Union[bytes, str]:
    """XOR 処理 (Hex文字列 / 単一バイト / マルチバイト / 文字列キー対応)

    :param decode: True の場合、結果を str で返します。
    :param encoding: decode=True の場合に使用する文字コード。
    :param errors: デコード失敗時の挙動 ("ignore", "replace", "strict" など)。
    """

    def _to_bytes(v):
        if isinstance(v, str):
            # "0x42" や "0X42" 表記の判定
            if v.startswith(("0x", "0X")):
                return bytes([int(v, 16) & 0xFF])
            # 16進数文字列 (例: "466c6167") の変換試行
            try:
                return bytes.fromhex(v)
            except ValueError:
                return v.encode()
        elif isinstance(v, int):
            return bytes([v & 0xFF])
        return bytes(v)

    data_bytes = _to_bytes(data)
    key_bytes = _to_bytes(key)

    if not key_bytes:
        raise ValueError("Key cannot be empty")

    res = bytes(b ^ k for b, k in zip(data_bytes, cycle(key_bytes)))

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
