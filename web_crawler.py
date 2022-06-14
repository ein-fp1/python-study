import requests
from bs4 import BeautifulSoup


def print_rank(rows):
    for row in rows:
        print(*row)


url = 'https://sports.news.naver.com/kbaseball/index'

response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.select_one('#rank_template1 > div > div.hmb_tbl > table > tbody')
    trs = tbody.select('tr')
    datas = []

    for tr in trs:
        rank = tr.select_one('th > span > em > span').get_text()
        team_name = tr.select_one('td > div > div.info > span').get_text()
        stats = tr.select('td > span')
        number_of_matches = int(stats[0].get_text())
        number_of_wins = int(stats[1].get_text())
        number_of_draws = int(stats[2].get_text())
        victory_points = int(stats[3].get_text())
        win_rate = float(stats[4].get_text())

        datas.append([rank, team_name, number_of_matches, number_of_wins, number_of_draws, victory_points, win_rate])

    print_rank(datas)
else:
    print(response.status_code)


