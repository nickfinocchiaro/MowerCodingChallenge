import strawberry
from typing import List, Tuple, Optional
from lawnmower.simulator import LawnMowerSimulator

@strawberry.type
class SimulationResult:
    all_grass_cut: bool
    uncut_grass_remaining: int
    crashed: bool
    crash_reason: Optional[str]

@strawberry.type
class Query:
    @strawberry.field
    def simulate(
        self,
        width: int,
        height: int,
        rocks: List[List[int]],  # Accept as list of lists from GraphQL query
        path: List[str]
    ) -> SimulationResult:
        rocks_tuples = [tuple(rock) for rock in rocks]  # Convert to list of tuples because LawnMowerSimulator expects tuples for dictionary keys
        sim = LawnMowerSimulator(width=width, height=height, rocks=rocks_tuples)
        result = sim.simulate(path)
        return SimulationResult(**result)

    @strawberry.field
    def hello(self) -> str:
        return "Welcome to the Robotic Lawnmower Simulator!"
