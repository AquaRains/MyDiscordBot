import urllib
import urllib.request


def webReq():
    f = urllib.request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3114051000')

    fstr = f.read().decode('utf-8')
    fstrarr = fstr.split('\n')
    print(fstrarr)


def main():
    webReq()
    pass


if __name__ == '__main__':
    main()
