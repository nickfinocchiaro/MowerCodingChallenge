"""
Simulator.py Simulates a robotic lawnmower navigating a grid, cutting grass, 
and handling obstacles.
"""
from typing import List, Tuple, Dict

# Define grid cell types
UNCUT = "uncut"
CUT = "cut"
ROCK = "rock"

# Define directions
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

class LawnMowerSimulator:
    """
    Class LawnMowerSimulator defines the following fields:
    - width: Width of the lawn grid
    - height: Height of the lawn grid
    - rocks: List of tuples representing rock positions
    - grid: Dictionary representing the lawn grid with cell states
    - position: Current position of the mower
    - crashed: Boolean indicating if the mower has crashed
    - crash_reason: Reason for the crash if it occurs
    """
    def __init__(self, width: int, height: int, rocks: List[Tuple[int, int]]):
        self.width = width
        self.height = height
        self.grid = self._initialize_grid(rocks)
        self.position = (0, 0)
        self.crashed = False
        self.crash_reason = None
        self._cut_grass(self.position)

    # Initialize the grid with uncut grass and place rocks
    # Rocks are represented as tuples of (row, column)
    def _initialize_grid(self, rocks: List[Tuple[int, int]]) -> Dict[Tuple[int, int], str]:
        grid = {(r, c): UNCUT for r in range(self.height) for c in range(self.width)}
        for rock in rocks:
            grid[rock] = ROCK
        return grid

    # Cut grass at the current position
    # If the grass is already cut, it remains cut
    def _cut_grass(self, pos: Tuple[int, int]):
        if self.grid.get(pos) == UNCUT:
            self.grid[pos] = CUT

    def _move(self, direction: str):
        if self.crashed:
            return

        if direction not in DIRECTIONS:
            #invalid directions are ignored, move to next direction
            return

        delta = DIRECTIONS[direction]
        new_pos = (self.position[0] + delta[0], self.position[1] + delta[1])

        # Check boundary of grid
        if not (0 <= new_pos[0] < self.height and 0 <= new_pos[1] < self.width):
            self.crashed = True
            self.crash_reason = "Crashed into fence"
            return

        # Check rock
        if self.grid.get(new_pos) == ROCK:
            self.crashed = True
            self.crash_reason = "Crashed into rock"
            return

        self.position = new_pos
        self._cut_grass(new_pos)

    def simulate(self, path: List[str]) -> Dict:
        """Simulate the path, cutting grass and checking for crashes returning the result"""
        for step in path:
            self._move(step)

        uncut_grass = sum(1 for cell in self.grid.values() if cell == UNCUT)

        return {
            "all_grass_cut": uncut_grass == 0 and not self.crashed,
            "uncut_grass_remaining": uncut_grass,
            "crashed": self.crashed,
            "crash_reason": self.crash_reason
        }
