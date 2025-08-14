import pytest
from lawnmower.graphql_schema import Query, SimulationResult

@pytest.fixture
def query():
    return Query()

# Test hello field

def test_hello_returns_welcome(query):
    assert query.hello() == "Welcome to the Robotic Lawnmower Simulator!"

# Test simulate field with no rocks, all grass cut

def test_simulate_all_grass_cut(query):
    result = query.simulate(
        width=2,
        height=2,
        rocks=[],
        path=["right", "down", "left", "up"]
    )
    assert isinstance(result, SimulationResult)
    assert result.all_grass_cut is True
    assert result.uncut_grass_remaining == 0
    assert result.crashed is False
    assert result.crash_reason is None

# Test simulate field with rocks, mower crashes

def test_simulate_crash_on_rock(query):
    result = query.simulate(
        width=2,
        height=2,
        rocks=[[0,1]],
        path=["right"]
    )
    assert result.all_grass_cut is False
    assert result.crashed is True
    assert result.crash_reason == "Crashed into rock"

# Test simulate field with mower crashing into fence

def test_simulate_crash_on_fence(query):
    result = query.simulate(
        width=2,
        height=2,
        rocks=[],
        path=["up"]
    )
    assert result.all_grass_cut is False
    assert result.crashed is True
    assert result.crash_reason == "Crashed into fence"

# Test simulate field with uncut grass remaining

def test_simulate_uncut_grass_remaining(query):
    result = query.simulate(
        width=2,
        height=2,
        rocks=[],
        path=["right"]
    )
    assert result.all_grass_cut is False
    assert result.uncut_grass_remaining > 0
    assert result.crashed is False
    assert result.crash_reason is None
