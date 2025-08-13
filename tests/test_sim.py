from lawnmower.simulator import LawnMowerSimulator

def test_basic_path():
    # 3x3 grid, no rocks
    sim = LawnMowerSimulator(width=3, height=3, rocks=[])
    path = ["right", "right", "down", "down", "left", "left", "up", "right"]
    result = sim.simulate(path)
    assert result['all_grass_cut'] is True
    assert result['uncut_grass_remaining'] == 0
    assert result['crashed'] is False
    assert result['crash_reason'] is None

def test_crash_into_rock():
    # 3x3 grid, rock at (0,1)
    sim = LawnMowerSimulator(width=3, height=3, rocks=[(0, 1)])
    path = ["right"]
    result = sim.simulate(path)
    assert result['all_grass_cut'] is False
    assert result['uncut_grass_remaining'] > 0
    assert result['crashed'] is True
    assert result['crash_reason'] == "Crashed into rock"

def test_crash_into_fence():
    # 2x2 grid, try to go out of bounds
    sim = LawnMowerSimulator(width=2, height=2, rocks=[])
    path = ["up"]
    result = sim.simulate(path)
    assert result['all_grass_cut'] is False
    assert result['uncut_grass_remaining'] > 0
    assert result['crashed'] is True
    assert result['crash_reason'] == "Crashed into fence"

def test_partial_cut():
    # 2x2 grid, skip one cell
    sim = LawnMowerSimulator(width=2, height=2, rocks=[])
    path = ["right", "down"]
    result = sim.simulate(path)
    assert result['all_grass_cut'] is False
    assert result['uncut_grass_remaining'] == 1
    assert result['crashed'] is False
    assert result['crash_reason'] is None

def test_invalid_direction():
    # 2x2 grid, invalid direction
    sim = LawnMowerSimulator(width=2, height=2, rocks=[])
    path = ["right", "diagonal", "down"]
    result = sim.simulate(path)
    assert result['all_grass_cut'] is False
    assert result['uncut_grass_remaining'] > 0
    assert result['crashed'] is False
    assert result['crash_reason'] is None
