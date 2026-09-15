def xor_brute(enc_data, knownstr=None):
    # データが str の場合は bytes に変換
    if isinstance(enc_data, str):
        enc_data = enc_data.encode()

    # knownstr が渡されていて str の場合は bytes に変換
    if isinstance(knownstr, str):
        knownstr = knownstr.encode()

    results = []

    # 単一バイトキー(0〜255)でのブルートフォース
    for key in range(256):
        decrypted = bytes([b ^ key for b in enc_data])

        # knownstr の指定がない、または解読結果に含まれている場合
        if knownstr is None or knownstr in decrypted:
            results.append((key, decrypted))

    return results



