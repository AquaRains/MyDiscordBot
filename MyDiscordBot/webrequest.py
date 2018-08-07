import urllib
import urllib.request
import xml.etree.ElementTree as et


def webReq():
    # f = urllib.request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159')

    zonecodes = {
        '전국': '108',
        '서울, 경기도': '109',
        '강원도': '105',
        '충청북도': '131',
        '충청남도': '133',
        '경상북도': '143',
        '전라북도': '146',
        '전라남도': '156',
        '경상남도': '159',
        '제주도': '184'}

    value = {'stnId': zonecodes['전국']}
    f = urllib.request.urlopen(
        'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3114051000' + '?' + urllib.parse.urlencode(value))

    fstr = f.read().decode('utf-8')

    tree = et.fromstring(fstr)
    for a in tree.getiterator():
        print(a)

    tree.find()
def main():
    webReq()
    pass


if __name__ == '__main__':
    main()
