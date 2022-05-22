import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

data_path_regu = "./data"
data_path_fall = "./data/fall"
data_path_rise = "./data/rise"
data_space_regu = os.listdir(data_path_regu)
data_space_fall = os.listdir(data_path_fall)
data_space_rise = os.listdir(data_path_rise)

date = ["2020/03", "2020/06", "2020/09", "2020/12"]

data_rise_sum = pd.read_csv(f"{data_path_regu}/exted_code_rise.csv")
data_rise_detail = pd.read_csv(f"{data_path_rise}/{data_space_rise[0]}")

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Date" : ["2020년 3월", "2020년 6월", "2020년 9월", "2020년 12월"],
    "Sales" : data_rise_detail["매출액"][5:9],
    "profit" : data_rise_detail["당기순이익"][5:9]
})

fig = px.bar(df, x="Date", y="Sales", barmode="group", width=700)

# children은 list로, style은 dict로 줘야됩니다.
app.layout = html.Div(children=[
    html.H1("Good Day, Sir."),
    dcc.Graph(figure=fig, style={"width" : "700"})
])

if __name__ == '__main__':
    app.run_server(debug=True)
