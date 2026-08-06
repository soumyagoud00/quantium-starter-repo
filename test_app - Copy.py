import pytest
from dash import Dash
from app import app


@pytest.fixture
def dash_duo(dash_duo):
    return dash_duo


def test_header_present(dash_duo):

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header.text == "Pink Morsel Sales Dashboard"



def test_visualisation_present(dash_duo):

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None



def test_region_picker_present(dash_duo):

    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-filter")

    assert picker is not None