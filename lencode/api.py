from urllib import parse


def url_encode(content: str):
    result = parse.quote(content)
    return result


def url_decode(content: str):
    result = parse.unquote(content)
    return result
