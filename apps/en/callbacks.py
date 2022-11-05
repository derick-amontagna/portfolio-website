from app import app
from dash import Input, Output
from apps.en.layouts import home
from apps.en.layouts import education
from apps.en.layouts import projects
from apps.en.layouts import publications
from apps.en.layouts import work_experience
from apps.en.layouts import skills
from apps.en.layouts import social_media

@app.callback(Output("page-content-en", "children"), [Input("url-en", "pathname")])
def render_page_content_en(pathname):
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