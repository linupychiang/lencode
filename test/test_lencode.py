from lencode.api import *

if __name__ == '__main__':
    content = '你好，世界'
    result = url_encode(content)
    print(result)
    result = url_decode(result)
    print(result)
