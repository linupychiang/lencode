from lencode import *

if __name__ == '__main__':
    content = '你好，世界'
    result = url_encode(content)
    print(result)
    result = url_decode(result)
    print(result)
    print(base64_encode('你好，世界'))
    print(base64_decode('5L2g5aW977yM5LiW55WM'))
