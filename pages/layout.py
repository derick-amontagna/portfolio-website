from dash import html, dcc
import dash_bootstrap_components as dbc
import pages.components as cp


image_path = "assets/indice.png"

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(cp.navbar)),
        # Title
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""# Derick Abreu Montagna, ElecEng"""), style={"textAlign": "center"}
            )
        ),
        # Resume
        dbc.Row(dbc.Col(dcc.Markdown("""##### *Resume* """), style={"textAlign": "center"})),
        dbc.Row(
            dbc.Col(
                html.Img(src=image_path, style={"--m": "8", "--tan": "0.41"}),
                style={"textAlign": "center"},
            )
        ),
        # Summary
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Summary """, id="summary"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(dbc.Alert(dcc.Markdown(open("data/summary.txt", "r").read()), color="dark"))
        ),
        # Education
        html.Hr(className="my-2"),
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Education """, id="education"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/education.txt", "r").read()), style={"textAlign": "left"}
            )
        ),
        # Publications
        html.Hr(className="my-2"),
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Selected Publications and Preprints """, id="publications"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/publications.txt", "r").read()), style={"textAlign": "left"}
            )
        ),
        # Work Experience
        html.Hr(className="my-2"),
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Work Experience """, id="workExperience"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/workExperience.txt", "r").read()),
                style={"textAlign": "left"},
            )
        ),
        # Skills
        html.Hr(className="my-2"),
        dbc.Row(dbc.Col(dcc.Markdown("""## Skills """, id="skills"), style={"textAlign": "left"})),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/skills.txt", "r").read()), style={"textAlign": "left"})
        ),
        # Projects
        html.Hr(className="my-2"),
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Projects """, id="projects"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/projects.txt", "r").read()), style={"textAlign": "left"}
            )
        ),
        # Social Media
        html.Hr(className="my-2"),
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Social Media """, id="social"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/social.txt", "r").read()), style={"textAlign": "left"})
        ),
    ]
)
