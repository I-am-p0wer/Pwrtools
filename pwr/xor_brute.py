from typing import Union, List, Tuple, Optional
from .xor import xor

def xor_brute(
    enc_data: Union[str, bytes, bytearray], 
    knownstr: Optional[Union[str, bytes]] = None
) -> List[Tuple[int, bytes]]:
    """1バイトキー (0〜255) でのブルートフォース"""
    
    # knownstr が str の場合は bytes に変換
    if isinstance(knownstr, str):
        knownstr = knownstr.encode()

    results = []

    for key in range(256):
        # xor 関数を利用して復号
        decrypted = xor(enc_data, key)

        # knownstr の指定がない、または解読結果に含まれている場合
        if knownstr is None or knownstr in decrypted:
            results.append((key, decrypted))

    return results
