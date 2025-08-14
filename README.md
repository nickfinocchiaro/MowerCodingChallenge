# LoftOrbital_MowerCodingChallenge
Coding Challenge for loft orbital Sr. Software Position

## Introduction
This repo simulates a robotic lawnmower based on the specifications from the [Robotic Lawnmower Homework Question](https://loftorbital.atlassian.net/wiki/external/MWVmZDQyYjUxMWIwNGZhZWI1YjRjNjkyYTkyZTNlNGU#%E2%9C%85-Evaluation-Criteria)

The goal of this project is to simulate a the mowing of a lawn, given the size of the gridded in width and height, a series of input directional steps for the mower, and locations of the rocks via a graphQL query. The resulting simulation will then respond to the query with retun information stating if all of the grass was cut, how many uncut squares in the grid remain, if the mower crashed while mowing, and what the mower crashed into (fence or rock).

## Design
The robitic lawnmower sim is a python based microservice that uses `FastAPI` to handle server logic, `Strawberry` to define `GraphQL` schemas that integrate with `FastAPI`, and `uvicorn` which is an ASGI web server that handles web connections from an api client or browser which in turn, allows `FastAPI` to serve the request. 

The microservice is contained within a docker container and uses `Docker-Compose` to simplify building and running for the user. 
## Setup
Follow the steps below to run the FastAPI microservice via Docker Compose:
1. Clone the repo or download it as a zip:
```bash
git clone https://github.com/nickfinocchiaro/LoftOrbital_MowerCodingChallenge.git
```

2. Open a terminal and ensure that Docker-Compose is installed by running the following command:
```bash
docker-compose --version
```

If you need to install docker compose follow the below steps for your operating system:\
**Ubuntu/Linux**
```bash
sudo apt-get install docker-compose
```

**Windows**\
Go to the [Docker Website](https://docs.docker.com/desktop/setup/install/windows-install/), download Docker Desktop for Windows, and follow the setup instructions. Run the version check command to ensure docker is installed before moving to the next step.

3. Once cloned, in the top level of the repo run the following docker-compose command via the command line to build and run the docker container:
```bash
docker-compose up --build
```

4. Verify the microservice is running. Open a web browser and navigate to the address below:
```html
http://localhost:8000/graphql
```
## Interacting with the API

## Tests
Follow the steps below to run test suite locally in a python virtual environment:
1. At the top level of the repo, create Python Virtual enviornment:
```bash
python -m venv .venv
```
2. Start the python virtual environment:
```bash
.venv\Scripts\activate
```
3. Install the developer requirements to the virtual environment:
```bash
pip install -e .[dev]
```
4. At the top level, run the following command to run the test suite:
```bash
pytest --cov --cov-report=html
``` 
5. To view unit test coverage report navigate to the `coverage` directory and open `class_index.html` in a web browser
