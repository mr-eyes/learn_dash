import dash
import dash_cytoscape as cyto
import dash_html_components as html


from dash.dependencies import Input, Output, State
import dash_core_components as dcc

cyto.load_extra_layouts()


# import elements
from get_elements import get_elements

app = dash.Dash(__name__)

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