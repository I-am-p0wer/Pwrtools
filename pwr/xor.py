from typing import Union, Sequence
from itertools import cycle

def xor(
    data: Union[str, bytes, bytearray, int, Sequence[int]],
    key: Union[str, bytes, bytearray, int, Sequence[int]],
    decode: bool = False,
    encoding: str = "utf-8",
    errors: str = "ignore"
) -> Union[bytes, str]:
    """強化版 XOR 処理 (0xHex / 0bBin / マルチバイトint / リスト / バイト列 / 文字列対応)"""

    def _to_bytes(v):
        if isinstance(v, str):
            # 1. 16進数文字列 (0x / 0X)
            if v.startswith(("0x", "0X")):
                hex_str = v[2:]
                if len(hex_str) % 2 != 0:
                    hex_str = "0" + hex_str
                return bytes.fromhex(hex_str)

            # 2. 2進数文字列 (0b / 0B)
            elif v.startswith(("0b", "0B")):
                bin_str = v[2:]
                pad_len = (8 - (len(bin_str) % 8)) % 8
                bin_str = ("0" * pad_len) + bin_str
                return bytes(
                    int(bin_str[i : i + 8], 2)
                    for i in range(0, len(bin_str), 8)
                )

            # 3. プレーンテキスト
            return v.encode(encoding)

        elif isinstance(v, int):
            # 0x1234 や 65535 などのマルチバイト数値にも自動対応
            length = (v.bit_length() + 7) // 8 or 1
            return v.to_bytes(length, byteorder="big")

        elif isinstance(v, (list, tuple)):
            # [0x41, 0x42] などの数値リストに対応
            return bytes(v)

        return bytes(v)

    data_bytes = _to_bytes(data)
    key_bytes = _to_bytes(key)

    if not key_bytes:
        raise ValueError("Key cannot be empty")

    res = bytes(b ^ k for b, k in zip(data_bytes, cycle(key_bytes)))

    if decode:
        return res.decode(encoding=encoding, errors=errors)

    return res
