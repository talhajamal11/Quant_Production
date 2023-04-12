import pandas as pd
from plotly import graph_objects as go
from plotly.subplots import make_subplots as ms
from matplotlib import pyplot as plt


class Plots:
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
            fig = fig.add_trace(go.Scatter(x=self.df.index,
                                     y=line
                                     )
                          )
        return fig

    def plot_macd(self,
                  macd: pd.Series,
                  signal: pd.Series,
                  hist: pd.Series,
                  price: str = 'Adj Close') -> plt.plot:
        fig_1 = plt.subplot2grid((8, 1), (0, 0), rowspan=5, colspan=1)
        fig_1.plot(self.df[price])

        fig_2 = plt.subplot2grid((8, 1), (5, 0), rowspan=3, colspan=1)
        fig_2.plot(macd, color='grey', linewidth=1.5, label='MACD')
        fig_2.plot(signal, color='skyblue', linewidth=1.5, label='SIGNAL')

        for i in range(len(self.df[price])):
            if str(hist[i])[0] == '-':
                fig_2.bar(self.df[price].index[i], hist[i], color='#ef5350')
            else:
                fig_2.bar(self.df[price].index[i], hist[i], color='#26a69a')

        plt.legend(loc='lower right')
        return None
