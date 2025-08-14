# Loft Orbital Mower Simulation Coding Challenge
Coding Challenge for Loft Orbital Sr. Software Position

## Introduction
This repo simulates a robotic lawnmower based on the specifications from the [Robotic Lawnmower Homework Question](https://loftorbital.atlassian.net/wiki/external/MWVmZDQyYjUxMWIwNGZhZWI1YjRjNjkyYTkyZTNlNGU#%E2%9C%85-Evaluation-Criteria)

The goal of this project is to simulate a the mowing of a lawn, given the size of the gridded in width and height, a series of input directional steps for the mower, and locations of the rocks via a graphQL query. The resulting simulation will then respond to the query with retun information stating if all of the grass was cut, how many uncut squares in the grid remain, if the mower crashed while mowing, and what the mower crashed into (fence or rock).

## Design
The robitic lawnmower sim is a Python module based microservice. It uses `FastAPI` to handle server logic, `Strawberry` to define `GraphQL` schemas that integrate with `FastAPI`, and `uvicorn` to run the webserver. 

The microservice is contained within a docker container using the python 3.13-alpine image because of it is ultra lightweight, allowing for quicker builds, faster pulls, and less disk usage.

I then opted to use `Docker-Compose` to simplify building and running for the user requiring only one command to build and run the microservice. 

Furthermore, I added Kubernetes manifest to make it deployable to a Kubernetes cluster. 
## Setup
### Docker Compose
Follow the steps below to run the FastAPI microservice via Docker Compose:
1. Clone the repo or download it as a zip:
```bash
git clone https://github.com/nickfinocchiaro/LoftOrbital_MowerCodingChallenge.git
```

2. Open a terminal and ensure that Docker-Compose is installed by running the following command:
```bash
docker-compose --version
```

If you need to install docker compose follow the below steps for your operating system:

**Ubuntu/Linux**\
Go to the [Docker Website](https://docs.docker.com/engine/install/ubuntu/), download Docker Desktop for Ubuntu, and follow the setup instructions. Run the version check command to ensure docker is installed before moving to the next step.

**Windows**\
Go to the [Docker Website](https://docs.docker.com/desktop/setup/install/windows-install/), download Docker Desktop for Windows, and follow the setup instructions. Run the version check command to ensure docker is installed before moving to the next step.

3. Once cloned, in the top level of the repo run the following docker-compose command via the command line to build and run the docker container:
```bash
docker-compose up --build -d
```

4. Verify the microservice is running. Open a web browser and navigate to the address below:
```html
http://localhost:8000/graphql
```
### Kuberenetes
Prerequesites for running this applicaiton in a Kubernetes cluster would be to have either `Minikube` or `Kind` installed for running a Kubernetes cluster on your local system. 

With the local cluster running follow the steps below:\
1. Apply the Kubernetes manifest:
```yml
kubectl apply -f k8s-deployment.yaml
```
2. Enable port for expected localhost port:
```yml
kubectl port-forward svc/lawnmower-service 8000:8000
```
3. Verify the microservice is running. Open a web browser and navigate to the address below:
```html
http://localhost:8000/graphql
```

## Interacting with the API
Continuing from the setup steps you will see a graphQL interface in the web browser. 

On the left hand side of the screen navigate select `Expand GraphiQL Explorer` to show the GraphQL query explorer. This is where the GraphQL UI will show you what types of queries are available to you for this application.

Here is an example query that can be pasted into the interface:
```GraphQL
query Simulate {
    simulate(width: 3, height: 3, rocks: [[1,1]], path: ["right","right","down","left","left","up"]) {
        allGrassCut
        uncutGrassRemaining
        crashed
        crashReason
    }
}
```

The resulting response for this query will look like this:
```GraphQL
{
    "data": {
        "simulate": {
            "allGrassCut": false,
            "uncutGrassRemaining": 4,
            "crashed": true,
            "crashReason": "Crashed into rock"
        }
    }
}
```

As an alternative, you may want to use [Postman](https://www.postman.com/) for easily creating, duplicating, and tracking requests. I tested this both using `Postman` and `GraphiQL` and preferred `Postman` for this process due to it's more intuitive UI and easy way to create a collection of requests. 

## Development Setup
I have integrated CI via GitHub actions for this project and you can see the results on the `Actions` tab of the repo which runs pylint, mypy and runs the unit test suite.

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
## Tests
At the top level, run the following command to run the test suite:
```bash
pytest --cov --cov-report=html
``` 
To view unit test coverage report navigate to the `coverage` directory and open `class_index.html` in a web browser
