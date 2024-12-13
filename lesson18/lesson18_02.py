from dash import Dash,html,dcc,callback,Input,Output,dash_table,_dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__,external_stylesheets=dmc.styles.ALL)
#radio button 要的資料
radio_data = [['pop','人口'],['lifeExp','平均壽命'],['gdpPercap','GDP']]
#selected 要的資料
selected_data = [{'value':value,"label":value} for value in df.country.unique()]

#Linechart圖表要的資料
# data = [
#         {"date": "Mar 22", "Apples": 2890, "Oranges": 2338, "Tomatoes": 2452},
#         {"date": "Mar 23", "Apples": 2756, "Oranges": 2103, "Tomatoes": 2402},
#         {"date": "Mar 24", "Apples": 3322, "Oranges": 986, "Tomatoes": 1821},
#         {"date": "Mar 25", "Apples": 3470, "Oranges": 2108, "Tomatoes": 2809},
# ]



app.layout = dmc.MantineProvider(
    [
        # html.H1("Dash App 標題", style={"textAlign": 'center'})
        dmc.Container(
            # html.H1("Dash App標題",style={"textAlign":"center"}),
            dmc.Title(f"世界各國人口、壽命、GDP", order=2),
            fluid=True,
            ta="center",
            p=30
        )
    ,
        # dcc.RadioItems(['pop','lifeExp','gdpPercap'],value = 'pop',inline=True,id='radio_item')
    #,
        # dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
    #
        #dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
        dmc.Flex(
            [
                dmc.Stack(
                    [
                        # dcc.RadioItems(['pop','lifeExp','gdpPercap'],value = 'pop',inline=True,id='radio_item')
                        dmc.RadioGroup(
                            children=dmc.Group([dmc.Radio(l, value=k) for k, l in radio_data], my=10),
                            id="radio_item",
                            value="pop",
                            label="Select the item you are interesting in ",
                            size="md",
                            mb=10,
                        )
                    ,
                        # dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
                        dmc.Select(
                                    label="Select Country",
                                    # placeholder="Select one",
                                    id="dropdown-selection",
                                    value="Taiwan",
                                    data=selected_data,
                                    w=200,
                                    mb=10,
                        )
                    ]

                )
            ,
                # dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
                # dmc.Center(
                #     dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
                # ,
                #     w=500
                # )
                dmc.ScrollArea(
                    children = [],
                    h=300,
                    w='50%',
                    id = 'scrollarea'
                )
            ],
            direction={"base":"column","sm":"row"},
            gap={"base":"sm","sm":"lg"},
            justify={"base":"center"}
        )
    ,
        # dcc.Graph(id='graph-content')
        # dmc.Container(
        #     dcc.Graph(id='graph-content')
        # )
        dmc.Container(
                dmc.LineChart(
                            id = 'lineChart',
                            h=300,
                            dataKey="year",
                            data=None,
                            series =[],
                            curveType="monotone",
                            tickLine="xy",
                            withXAxis=True,
                            withDots=True,
                            gridAxis="xy",
                            withLegend=True,
                            xAxisLabel="年分",
                            yAxisLabel=[]


                ),
                my=50
        )
    ]
)

#圖表事件
@callback(
    Output('lineChart','data'),
    Output('lineChart','series'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
)
def update_graph(country_value,radio_value):
    #Linechart圖表要的資料
    dff = df[df.country == country_value]
    pop_diff=dff[['country','year',radio_value]]
    line_chart_data = pop_diff.to_dict('records')
    if radio_value =='pop':
        lable_title= f'{country_value}:人口成長圖表'
    elif radio_value =='lifeExp':
        lable_title = f'{country_value}:壽命'
    elif radio_value == 'gdpPercap':
        lable_title = f'{country_value}: 人均GDP'

    series= [
        {"name":radio_value,"label":lable_title,"color":"indigo.6"}
    ]

    return line_chart_data,series




# def update_graph(country_value,radio_value):    
#     dff = df[df.country ==country_value]
#     if radio_value =='pop':
#         title= f'{country_value}:人口成長圖表'
#     elif radio_value =='lifeExp':
#         title = f'{country_value}:壽命'
#     elif radio_value == 'gdpPercap':
#         title = f'{country_value}: 人均GDP'
#     return px.line(dff,x='year',y=radio_value,title=title)

# #表格事件
@callback(
    Output('scrollarea','children'),
    # Output('datatable','columns'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
)
def update_table(country_value,radio_value):
    print(country_value,radio_value)
    #只顯示台灣的資料
    dff = df[df.country ==country_value]
    pop_diff = dff[['country','year',radio_value]]
    elements = pop_diff.to_dict("records")

    rows = [ 
        dmc.TableTr(
            [
                dmc.TableTd(element["country"]),
                dmc.TableTd(element["year"]),
                dmc.TableTd(element[radio_value]),
            ]
        )
        for element in elements
    ]

    if radio_value=='pop':
        head_name = '人口'
    elif radio_value =='lifeExp':
        head_name = '壽命'
    elif radio_value =='gdpPercap':
        head_name = 'GDP'

    head = dmc.TableThead(
        dmc.TableTr(
            [
                dmc.TableTh("國家"),
                dmc.TableTh("年分"),
                dmc.TableTh(head_name)
            ]
        )
    )

    body = dmc.TableTbody(rows)
    caption = dmc.TableCaption(f"{head_name} Taiwan NO.1")
    return dmc.Table([head,body,caption])


if __name__ =='__main__':
    app.run(debug=True)