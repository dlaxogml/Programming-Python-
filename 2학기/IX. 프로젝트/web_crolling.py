from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    # 네이버 웹툰
    # data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559")
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=524520")
    soup = BeautifulSoup(data, "lxml")
    data.close()
    

    cartoon_titles = soup.find_all("td", attrs = {'class' : 'title'})
    html = "<html><head><meta charset='utf-8'></head><body>"
    for title in cartoon_titles:
        t = title.find('a').text
        link = title.find('a').get("href")
        link = "http://comic.naver.com/" + link
        # print(t)
        # print(link)
        # print("<a href='" + link + "'>" + t + "</a>")
        html += "<a href='" + link + "'>" + t + "</a><br>"
    html += "</body></html>"
    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("트럼프.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)

    # 다음 웹툰
    # data = urlopen("http://webtoon.daum.net/webtoon/view/findjuly")
    # soup = BeautifulSoup(data, "lxml")
    # print(soup)
    # cartoon_titles = soup.find_all{"strong", attrs = ("tit_wt"})
    # for title in cartoon_titles:
    #     print(title)