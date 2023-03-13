import pandas as pd
from plotly import graph_objects as go
from plotly.subplots import make_subplots as ms


class Ply:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe

    def price_vol(self, price: str, volume) -> go.Figure:
        fig = ms(specs=[[{"secondary_y": True}]])
        fig = fig.add_trace(go.Scatter(x=self.df.index,
                                       y=self.df[price],
                                       ),
                            secondary_y=False
                            )
        fig = fig.add_trace(go.Bar(x=self.df.index,
                                   y=self.df[volume],
                                   ),
                            secondary_y=True
                            )
        fig.update_yaxes(range=[0, 100000000], secondary_y=True)
        fig.update_yaxes(range=[0, 200], secondary_y=False)
        fig.show()

        return fig

    def multiple_line_chart(self,
                            list_series: list) -> go.Figure:
        for line in list_series:
            fig.add_trace(go.Scatter(x=self.df.index,
                                     y=line
                                     )
                          )
        return fig