import hashlib
from typing import Union

def _hash_digest(algo: str, data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """ハッシュ計算の共通内部処理"""
    if isinstance(data, str):
        data_bytes = data.encode(encoding)
    elif isinstance(data, (bytes, bytearray)):
        data_bytes = bytes(data)
    else:
        raise TypeError("Input must be str or bytes")

    h = hashlib.new(algo)
    h.update(data_bytes)
    return h.hexdigest()

def md5(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """MD5 ハッシュ値を生成"""
    return _hash_digest("md5", data, encoding)

def sha1(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """SHA1 ハッシュ値を生成"""
    return _hash_digest("sha1", data, encoding)

def sha256(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """SHA256 ハッシュ値を生成"""
    return _hash_digest("sha256", data, encoding)

def sha512(data: Union[str, bytes], encoding: str = "utf-8") -> str:
    """SHA512 ハッシュ値を生成"""
    return _hash_digest("sha512", data, encoding)
