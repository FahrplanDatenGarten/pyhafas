from Crypto.Cipher import AES
import base64

aid = "rGhXPq+xAlvJd8T8cMnojdD0IoaOY53X7DPAbcXYe5g=" # from res/raw/haf_config.properties; HCI_CHECKSUM
key = bytes([97, 72, 54, 70, 56, 122, 82, 117, 105, 66, 110, 109, 51, 51, 102, 85]) # from de/hafas/g/a/b.java of DBNavigator; probably static

unpad = lambda s : s[:-ord(s[len(s)-1:])] # http://stackoverflow.com/a/12525165/3890934
enc = base64.b64decode(aid)
iv = bytes([00]*16)
cipher = AES.new(key, AES.MODE_CBC, iv)
salt = unpad(cipher.decrypt(enc).decode("utf-8"))

print("Salt:", salt)
