import dash
import dash_cytoscape as cyto
import dash_html_components as html

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