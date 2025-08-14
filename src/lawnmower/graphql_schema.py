"""GraphQL schema for the Robotic Lawnmower Simulator
This module defines the GraphQL query types and fields for simulating a robotic lawnmower
It includes the SimulationResult type to encapsulate the results of a simulation,
and the Query type to handle simulation requests and return a welcome message."""
from typing import List, Optional
import strawberry
from lawnmower.simulator import LawnMowerSimulator

@strawberry.type
class SimulationResult:
    """    Class SimulationResult defines the following fields:
    - all_grass_cut: Boolean indicating if all grass was cut
    - uncut_grass_remaining: Number of uncut grass cells remaining
    - crashed: Boolean indicating if the mower has crashed
    - crash_reason: Optional reason for the crash if it occurs
    """
    all_grass_cut: bool
    uncut_grass_remaining: int
    crashed: bool
    crash_reason: Optional[str]

@strawberry.type
class Query:
    """GraphQL query type for the Robotic Lawnmower Simulator
    This class defines the fields available in the GraphQL schema:
    - simulate: Simulates the lawnmower's path and returns the result
    """
    @strawberry.field
    def simulate(
        self,
        width: int,
        height: int,
        rocks: List[List[int]],
        path: List[str]
    ) -> SimulationResult:
        """
        Query format for Simulating the lawnmower's movement on the grid.

        Args:
            width: Width of the grid.
            height: Height of the grid.
            rocks: List of rock positions as [row, col] represented as a list of lists.
            path: List of movement directions.

        Returns:
            SimulationResult: The result of the simulation:
            - all_grass_cut: True if all grass was cut, False otherwise.
            - uncut_grass_remaining: Number of uncut grass cells remaining.
            - crashed: True if the mower crashed, False otherwise.
            - crash_reason: Reason for the crash if it occurred, None otherwise.
        """
        # Convert to list of tuples LawnMowerSimulator expects tuples of (int, int)
        rocks_tuples = [(int(rock[0]), int(rock[1])) for rock in rocks if len(rock) == 2 and all(isinstance(x, int) for x in rock[:2])]
        sim = LawnMowerSimulator(width=width, height=height, rocks=rocks_tuples)
        result = sim.simulate(path)
        return SimulationResult(**result)
