import requests as req
from bs4 import BeautifulSoup
import csv


def get_some_code(url, name):
    company_name = []
    company_code = []

    r = req.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    td_title = soup.findAll("tr")
    for i in td_title:
        a_tag = i.find("a")
        a_tag_str = str(a_tag)
        if a_tag:
            company_name.append(a_tag.text)  # 회사명
        if a_tag_str.find("code") == 38:
            company_code.append(a_tag_str[43:49])  # 회사코드

    with open(f"./data/exted_code_{name}.csv", "w", newline='', encoding='utf-8') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerow(["index", "name", "code"])
        for i in range(0, len(company_code)):
            wr.writerow([i + 1, company_name[i], company_code[i]])
        csv_file.close()
