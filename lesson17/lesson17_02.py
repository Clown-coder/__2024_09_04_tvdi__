from dash import Dash,html,dcc,callback,Input,Output,dash_table,_dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__,external_stylesheets=dmc.styles.ALL)

radio_data = [['pop','人口'],['lifeExp','平均壽命'],['gdpPercap','GDP']]
selected_data = [{'value':value,"label":value} for value in df.country.unique()]
app.layout = dmc.MantineProvider(
    [
        # html.H1("Dash App 標題", style={"textAlign": 'center'})
        dmc.Container(
            # html.H1("Dash App標題",style={"textAlign":"center"}),
            dmc.Title(f"世界各國人口、壽命、GDP", order=2),
            fluid=True,
            ta="center",
            p=20
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
                                    placeholder="Select one",
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
                dmc.Center(
                    dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
                ,
                    w=500
                )
            ],
            direction={"base":"column","sm":"row"},
            gap={"base":"sm","sm":"lg"},
            justify={"base":"center"}
        )
    ,
        # dcc.Graph(id='graph-content')
        dmc.Container(
            dcc.Graph(id='graph-content')
        )
    ]
)

#圖表事件
@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
)
def update_graph(country_value,radio_value):
    dff = df[df.country ==country_value]
    if radio_value =='pop':
        title= f'{country_value}:人口成長圖表'
    elif radio_value =='lifeExp':
        title = f'{country_value}:壽命'
    elif radio_value == 'gdpPercap':
        title = f'{country_value}: 人均GDP'
    return px.line(dff,x='year',y=radio_value,title=title)

#表格事件
@callback(
    Output('datatable','data'),
    Output('datatable','columns'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
)
def update_table(country_value,radio_value):
    dff = df[df.country ==country_value]
    columns = [
        {'id':'country','name':'country'},
        {'id':'year','name':'year'}
    ]
    if radio_value =='pop':
        columns.append({'id':'pop','name':'pop'})
    elif radio_value =='lifeExp':
        columns.append({'id':'lifeExp','name':'lifeExp'})
    elif radio_value =='gdpPercap':
        columns.append({'id':'gdpPercap','name':'gdpPercap'})
    return dff.to_dict('records'),columns


if __name__ =='__main__':
    app.run(debug=True)