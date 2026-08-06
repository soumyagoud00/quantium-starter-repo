import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


# Read data
df = pd.read_csv("data/formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


app = Dash(__name__)


app.layout = html.Div(

    style={
        "backgroundColor": "#f2f6ff",
        "padding": "40px",
        "minHeight": "100vh",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#6a1b9a"
            }
        ),


        html.Div([

            html.Label(
                "Select Region",
                style={
                    "fontSize": "18px",
                    "fontWeight": "bold"
                }
            ),


            dcc.RadioItems(

                id="region-filter",

                options=[

                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"}

                ],

                value="all",

                inline=True
            )

        ]),


        dcc.Graph(
            id="sales-chart"
        )

    ]

)



@app.callback(

    Output("sales-chart", "figure"),

    Input("region-filter", "value")

)


def update_graph(region):

    if region == "all":

        data = df

    else:

        data = df[df["region"] == region]


    fig = px.line(

        data,

        x="date",

        y="sales",

        title="Pink Morsel Sales"

    )


    fig.update_layout(

        xaxis_title="Date",

        yaxis_title="Sales",

        template="plotly_white"

    )


    return fig




if __name__ == "__main__":

    app.run(debug=True)