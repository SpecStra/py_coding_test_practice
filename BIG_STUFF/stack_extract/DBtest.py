import pymysql
import pandas as pd
import os

directions = {
    "rise" : "https://finance.naver.com/sise/sise_rise.nhn",
    "fall" : "https://finance.naver.com/sise/sise_fall.nhn"
}

data_path = "./data"
data_space = os.listdir(data_path)
fall_path = "./data/fall"
rise_path = "./data/rise"
fall_space = os.listdir(fall_path)
rise_space = os.listdir(rise_path)

rise = rise_space[0:9]
fall = fall_space[0:9]

code = pd.read_csv(f"{data_path}/exted_code_rise.csv")
#print(code["code"][0])
#print(a["매출액"][0])

companyInfo_db = pymysql.connect(
    user="root",
    passwd='$$tkzksk45!@',
    host="127.0.0.1",
    db="company",
    charset="utf8"
)
company_cursor = companyInfo_db.cursor(pymysql.cursors.DictCursor)

print(code)

"""
#USE company;
#INSERT INTO fina_info VALUES (43245.0, 1050.0, -45.0, "002025")
#company_info 입력
for i in range(0, 9) :
    codes = str(code["code"][i])
    name = str(code["name"][i])
    business = str(code["business"][i])
    sql_query = f"INSERT INTO company_info VALUES (\"{codes}\", \"{name}\", \"{business}\");"
    company_cursor.execute(sql_query)
    companyInfo_db.commit()
    result = company_cursor.fetchall()
    print(result)

#fina_info 입력
for i in range(0, 9) :
    datas = pd.read_csv(f"{rise_path}/{rise[i]}")
    sales = datas["매출액"][i]
    oper_profit = datas["영업이익"][i]
    net_income = datas["당기순이익"][i]
    codes = str(code["code"][i])
    sql_query = f"INSERT INTO fina_info VALUES ({sales}, {oper_profit}, {net_income}, \"{codes}\")"
    company_cursor.execute(sql_query)
    companyInfo_db.commit()
    result = company_cursor.fetchall()
    print(result)


company_cursor = companyInfo_db.cursor(pymysql.cursors.DictCursor)
sql_qu = "SELECT * FROM `company_info`;"
company_cursor.execute(sql_qu)
result = company_cursor.fetchall()
print(result)
"""