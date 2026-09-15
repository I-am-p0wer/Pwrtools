from typing import Union

def from_hex(hex_str: str, decode: bool = False, encoding: str = "utf-8", errors: str = "ignore") -> Union[bytes, str]:
    """16進数文字列を bytes または str に変換 (デフォルト: bytes)"""
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string")
    
    clean_hex = hex_str.strip().replace("0x", "").replace("0X", "")
    clean_hex = clean_hex.replace(" ", "").replace(":", "").replace("\n", "")
    
    if len(clean_hex) % 2 != 0:
        clean_hex = "0" + clean_hex

    res = bytes.fromhex(clean_hex)

    if decode:
        return res.decode(encoding=encoding, errors=errors)
    
    return res
