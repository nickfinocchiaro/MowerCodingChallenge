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
        rocks: List[Tuple[int, int]],
        path: List[str]
    ) -> SimulationResult:
        sim = LawnMowerSimulator(width=width, height=height, rocks=rocks)
        result = sim.simulate(path)
        return SimulationResult(**result)
