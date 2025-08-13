from fastapi import FastAPI
from lawnmower.models import SimulationRequest, SimulationResponse
from lawnmower.simulator import LawnMowerSimulator

lawnmower_app = FastAPI(title="Roboitc Lawnmower Simulator")

@lawnmower_app.post("/simulate", response_model=SimulationResponse)
def simulate_lawn(request: SimulationRequest):
    sim = LawnMowerSimulator(
        width=request.width,
        height=request.height,
        rocks=request.rocks
    )
    result = sim.simulate(request.path)
    return SimulationResponse(**result)

#Health check endpoint
@lawnmower_app.get("/")
def heath():
    return "OK"