from pydantic import BaseModel
from typing import List, Tuple, Optional

class SimulationRequest(BaseModel):
    width: int
    height: int
    rocks: List[Tuple[int, int]]
    path: List[str]

class SimulationResponse(BaseModel):
    all_grass_cut: bool
    uncut_grass_remaining: int
    crashed: bool
    crash_reason: Optional[str]
