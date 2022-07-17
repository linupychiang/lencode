from base64 import b64encode, b64decode
from urllib import parse


def url_encode(content: str):
    result = parse.quote(content)
    return result


def url_decode(content: str):
    result = parse.unquote(content)
    return result


def base64_encode(content: str):
    st = content.encode()  # 默认以utf8编码
    result = b64encode(st)
    return result.decode()


def base64_decode(content: str):
    st = content.encode()  # 默认以utf8编码
    result = b64decode(st)
    return result.decode()
