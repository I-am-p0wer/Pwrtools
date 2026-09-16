from typing import Union

def rev(data: Union[str, bytes, bytearray], hexstr: bool = False) -> Union[str, bytes]:
    """文字列・バイト列・16進数文字列を反転 (リバース)
    
    :param data: 対象データ (str または bytes)
    :param hexstr: True の場合、16進数文字列として2文字単位で反転 (例: '4142' -> '4241')
    :return: 反転後のデータ (入力と同じ型、または str)
    """
    if hexstr:
        if isinstance(data, (bytes, bytearray)):
            s = data.decode("ascii")
        elif isinstance(data, str):
            s = data
        else:
            raise TypeError("Input must be str or bytes")

        clean_hex = s.strip().replace("0x", "").replace("0X", "").replace(" ", "")
        if len(clean_hex) % 2 != 0:
            clean_hex = "0" + clean_hex
        
        # 2文字(1バイト)ごとに分解して逆順に結合
        chunks = [clean_hex[i:i+2] for i in range(0, len(clean_hex), 2)]
        res_hex = "".join(reversed(chunks))
        
        return f"0x{res_hex}" if s.startswith(("0x", "0X")) else res_hex

    if isinstance(data, str):
        return data[::-1]
    elif isinstance(data, (bytes, bytearray)):
        return bytes(data[::-1])
    else:
        raise TypeError("Input must be str or bytes")
