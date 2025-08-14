"""Unit tests for the GraphQL schema of the Robotic Lawnmower Simulator

This module tests the Query type and its fields, including the simulate and hello methods.
It includes tests for various scenarios such as successful simulation, crashes due to rocks 
or fences, and checking grass cutting status.

It uses pytest for testing and checks the expected outcomes of the GraphQL queries.
"""
import pytest
from lawnmower.graphql_schema import Query, SimulationResult

@pytest.fixture(name="query")
def query():
    """Fixture to create an instance of the Query class for testing"""
    return Query()

def test_hello_returns_welcome(query_fixture):
    """Test that the hello field returns the expected welcome message"""
    assert query_fixture.hello() == "Welcome to the Robotic Lawnmower Simulator!"

def test_simulate_all_grass_cut(query_fixture):
    """Test simulate field with no rocks and all grass cut"""
    result = query_fixture.simulate(
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

def test_simulate_crash_on_rock(query_fixture):
    """Test simulate field with mower crashing into a rock"""
    result = query_fixture.simulate(
        width=2,
        height=2,
        rocks=[[0,1]],
        path=["right"]
    )
    assert result.all_grass_cut is False
    assert result.crashed is True
    assert result.crash_reason == "Crashed into rock"

def test_simulate_crash_on_fence(query_fixture):
    """Test simulate field with mower crashing into a fence"""
    result = query_fixture.simulate(
        width=2,
        height=2,
        rocks=[],
        path=["up"]
    )
    assert result.all_grass_cut is False
    assert result.crashed is True
    assert result.crash_reason == "Crashed into fence"

def test_simulate_uncut_grass_remaining(query_fixture):
    """Test simulate field with mower not cutting all grass"""
    result = query_fixture.simulate(
        width=2,
        height=2,
        rocks=[],
        path=["right"]
    )
    assert result.all_grass_cut is False
    assert result.uncut_grass_remaining > 0
    assert result.crashed is False
    assert result.crash_reason is None
