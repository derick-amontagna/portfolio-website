from app import app
from dash import Input, Output
from apps.pt.layouts import home
from apps.pt.layouts import education
from apps.pt.layouts import projects
from apps.pt.layouts import publications
from apps.pt.layouts import work_experience
from apps.pt.layouts import skills
from apps.pt.layouts import social_media

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
    elif pathname == "/Skills":
        return skills.layout
    elif pathname == "/Projects":
        return projects.layout
    elif pathname == "/Social-Media":
        return social_media.layout
    return home.layout