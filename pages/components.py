import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#home", external_link=True)),
        dbc.NavItem(dbc.NavLink("Education", href="#education", external_link=True)),
        dbc.NavItem(dbc.NavLink("Publications", href="#publications", external_link=True)),
        dbc.NavItem(dbc.NavLink("Work Experience", href="#workExperience", external_link=True)),
        dbc.NavItem(dbc.NavLink("Skills", href="#skills", external_link=True)),
        dbc.NavItem(dbc.NavLink("Projects", href="#projects", external_link=True)),
        dbc.NavItem(dbc.NavLink("Social Media", href="#social", external_link=True)),
    ],
    brand="Derick Abreu Montagna",
    color="dark",
    sticky="top",
    dark=True,
    class_name={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
)
