import dash
import dash_cytoscape as cyto
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


from dash.dependencies import Input, Output, State
import dash_core_components as dcc

cyto.load_extra_layouts()


# import elements
from get_elements import get_elements

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open("template.html" , 'r') as html:
    app.index_string = 

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-compound',
        layout={'name': 'random'},
        style={'width': '100%', 'height': '450px'},
        elements= get_elements()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)