import urllib
import urllib.request

def webReq():
    f = urllib.request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159')
    print(f.read().decode('utf-8'))


def main():
    webReq()
    pass

if __name__ == '__main__':
    main()