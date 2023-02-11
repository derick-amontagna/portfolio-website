from app import app
from dash import Input, Output
from apps.pt.layouts import home
from apps.pt.layouts import education
from apps.pt.layouts import projects
from apps.pt.layouts import publications
from apps.pt.layouts import work_experience
from apps.pt.layouts import contact


@app.callback(Output("page-content-pt", "children"), [Input("url-pt", "pathname")])
def render_page_content_pt(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/Education":
        return education.layout
    elif pathname == "/Publications":
        return publications.layout
    elif pathname == "/Work-Experience":
        return work_experience.layout
    elif pathname == "/Projects":
        return projects.layout
    elif pathname == "/Contact":
        return contact.layout
    return home.layout
