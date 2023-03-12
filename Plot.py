from plotly import graph_objects as go
import pandas as pd


class Ply:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe

    def line_chart(self,
                   y_axis: str) -> go.Figure:
        fig = go.Figure(data=go.Scatter(x=self.df.index,
                                        y=self.df[y_axis],
                                        mode='lines+markers'))
        fig.show()

        return fig
