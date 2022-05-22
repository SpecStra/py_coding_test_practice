import pandas as pd
import os
from extract_code import get_some_code
from data import extract_state

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

if "exted_code_rise.csv" in data_space:
    try:
        os.remove(f"{data_path}/exted_code_rise.csv")
        os.remove(f"{data_path}/exted_code_fall.csv")
        for i in fall_space:
            os.remove(f"{fall_path}/{i}")
        for i in rise_space:
            os.remove(f"{rise_path}/{i}")
    except FileNotFoundError:
        print()
    os.rmdir(f"{data_path}/fall")
    os.rmdir(f"{data_path}/rise")

if not os.path.exists(f"./data/rise"):
    os.makedirs(f"./data/rise")
    os.makedirs(f"./data/fall")

#0. 코드 찾기
for r_and_f in list(directions.keys()) :
    get_some_code(directions[r_and_f], r_and_f)


#1. 찾은 코드로 크롤링하여 csv화
exted_code_data_main = {}

data_path = "./data"
data_space = os.listdir(data_path)

for files in data_space:
    if ".csv" in files:
        exted_code_data_main[f"{files[:-4]}"] = pd.read_csv(f"{data_path}/{files}", dtype=str)

extract_state.get_info_and_write_csv(exted_code_data_main["exted_code_rise"], list(directions.keys())[0])
extract_state.get_info_and_write_csv(exted_code_data_main["exted_code_fall"], list(directions.keys())[1])
