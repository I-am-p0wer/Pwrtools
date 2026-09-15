from typing import Union, Iterable

def to_hex(
    data: Union[str, bytes, bytearray, int, Iterable[int]], 
    prefix: bool = False, 
    sep: str = "", 
    upper: bool = False
) -> str:
    """データを16進数文字列に変換
    
    :param data: 変換対象 (bytes, str, int, intのリストなど)
    :param prefix: True の場合、先頭に "0x" を付与
    :param sep: バイト間の区切り文字 (例: " ", ":")
    :param upper: True の場合、大文字の16進数表記 (例: 466C6167)
    """
    if isinstance(data, str):
        data_bytes = data.encode("utf-8")
    elif isinstance(data, int):
        # 0の場合は "00" と扱う
        data_bytes = bytes([data & 0xFF]) if data != 0 else b"\x00"
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    elif isinstance(data, Iterable):
        data_bytes = bytes([b & 0xFF for b in data])
    else:
        raise TypeError("Unsupported data type for to_hex")

    hex_str = data_bytes.hex()

    if upper:
        hex_str = hex_str.upper()

    if sep:
        # 2文字ごとに区切り文字を挿入
        hex_str = sep.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2))

    if prefix:
        return f"0x{hex_str}"

    return hex_str
