from base64 import b64encode, b64decode
from urllib import parse
import hashlib


def url_encode(content: str):
    result = parse.quote(content)
    return result


def url_decode(content: str):
    result = parse.unquote(content)
    return result


def base64_encode(content: str):
    st = content.encode()
    result = b64encode(st)
    return result.decode()


def base64_decode(content: str):
    st = content.encode()
    result = b64decode(st)
    return result.decode()


def md5(content: str):
    md = hashlib.md5()
    md.update(content.encode('u8'))
    return md.hexdigest()


def md5_file(file_content: bytes):
    md = hashlib.md5()
    md.update(file_content)
    return md.hexdigest()
