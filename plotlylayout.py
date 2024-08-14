#INFO: plotlyでよく使うレイアウトの設定，保存，描画などの関数をまとめておく．
import pathlib
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from typing import Dict, List


pio.templates.default = "plotly_white"

def save_and_plot(fig, filename:str='NoName', path:pathlib='./', format:List[str]=['svg', 'png']):
    for f in format:
        pio.write_image(fig, path/f'{filename}.{f}')
    fig.show()

def update_layout(fig, layout:Dict):
    fig.update_layout(layout)

def dark_mode():
    pio.templates.default = "plotly_dark"

def customize_layout():
    costum_template = dict(
        layout=go.Layout(
            height=400,
            width=400,
            plot_bgcolor='#E6E6E6',
            font=dict(family="PlemolJP", size=16, color="#585858"),
            title=dict(font=dict(size=26, color="#585858"), x=0.5, y=0.97),
            legend=dict(xanchor='left', yanchor='bottom', font=dict(size=16, color="#585858")),
            margin=dict(l=60, r=20, t=50, b=40),
            xaxis=dict(linewidth=1, linecolor="#424242", color="#424242", title_standoff=0.01),
            yaxis=dict(linewidth=1, linecolor="#424242", color="#424242", title_standoff=0.01),
        )
    )

    # テンプレを適用
    pio.templates["costum_template"] = costum_template
    pio.templates.default = "costum_template"