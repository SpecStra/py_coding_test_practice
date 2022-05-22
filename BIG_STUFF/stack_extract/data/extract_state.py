import csv
import requests as req
from bs4 import BeautifulSoup
import re

base_url = "https://finance.naver.com/item/main.nhn?code="
not_a_value = ""


def get_info_and_write_csv(pandas_data, height):
    # 정보를 모두 담을 list
    all_infor_arry = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]

    def extract_info(url):
        # 날짜(time), 각종 주가정보(gold)
        r = req.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        st_table = soup.findAll("table")
        try:
            st_time = st_table[3].find("thead").findAll("th")
            st_golds = st_table[3].find("tbody").findAll("td")

            re_form = re.compile('20.....')
            gd_form = re.compile(r'((-)?\d{1,3}(,\d{3})*(\.\d+)?)')

            # 날짜 추출
            for i in st_time[3:12]:
                se_form = re_form.search(i.text)
                all_infor_arry[0].append(se_form.group())

            # 나머지 모든 정보 추출
            for i in range(0, 13):
                for j in st_golds[i * 10:(i * 10) + 9]:
                    try:
                        all_infor_arry[i + 1].append(gd_form.search(j.text).group().replace(",", ""))
                    except AttributeError:
                        all_infor_arry[i + 1].append("")
        except AttributeError:
            print("정보없음")
            pass
        except IndexError:
            print("정보부족")
            pass

    for i in range(0, 100):
        all_infor_arry = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
        info_url = base_url + pandas_data["code"][i]
        print(info_url)
        extract_info(info_url)
        file_name = pandas_data["name"][i]
        try:
            if all_infor_arry[2][0]:
                with open(f"./data/{height}/exted_info_{0 if i < 9 else not_a_value}{i + 1}_{file_name}.csv", "w",
                          newline='', encoding='utf-8') as csv_file:
                    wr = csv.writer((csv_file))
                    wr.writerow(
                        ["날짜", "매출액", "영업이익", "당기순이익", "영업이익률", "순이익률", 'ROE', "부채비율", "당좌유보", "유보율", "EPS", "PER",
                         "BPS", "PBR"])
                    for j in range(0, len(all_infor_arry[0])):
                        wr.writerow(
                            [f"{all_infor_arry[0][j]}", f"{all_infor_arry[1][j]}", f"{all_infor_arry[2][j]}",
                             f"{all_infor_arry[3][j]}",
                             f"{all_infor_arry[4][j]}", f"{all_infor_arry[5][j]}", f"{all_infor_arry[6][j]}",
                             f"{all_infor_arry[7][j]}",
                             f"{all_infor_arry[8][j]}", f"{all_infor_arry[9][j]}", f"{all_infor_arry[10][j]}",
                             f"{all_infor_arry[11][j]}",
                             f"{all_infor_arry[12][j]}", f"{all_infor_arry[13][j]}"])
                    csv_file.close()
        except IndexError:
            print(f"정보 부족으로 {i}번째 csv 패스")
