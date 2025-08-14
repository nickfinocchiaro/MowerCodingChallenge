# LoftOrbital_MowerCodingChallenge
Coding Challenge for loft orbital Sr. Software Position

## Introduction
This repo simulates a robotic lawnmower based on the specifications from the [Robotic Lawnmower Homework Question](https://loftorbital.atlassian.net/wiki/external/MWVmZDQyYjUxMWIwNGZhZWI1YjRjNjkyYTkyZTNlNGU#%E2%9C%85-Evaluation-Criteria)

The goal of this project is to simulate a the mowing of a lawn, given the size of the gridded in width and height, a series of input directional steps for the mower, and locations of the rocks via a graphQL query. The resulting simulation will then respond to the query with retun information stating if all of the grass was cut, how many uncut squares in the grid remain, if the mower crashed while mowing, and what the mower crashed into (fence or rock).
## Setup
Follow the steps below to run the microservice via Docker Compose:
1. Clone the repo or download it as a zip:\
`git clone https://github.com/nickfinocchiaro/LoftOrbital_MowerCodingChallenge.git`

2. Open a terminal and ensure that Docker-Compose is installed by running the following command:\
`docker-compose --version`

    If you need to install docker compose follow the below steps for your operating system:\
    **Ubuntu/Linux**\
    `sudo apt-get install docker-compose`

    **Windows**\
    Go to the [Docker Website](https://docs.docker.com/desktop/setup/install/windows-install/), download Docker Desktop for Windows, and follow the setup instructions. Run the version check command to ensure docker is installed before moving to the next step.

3. Once cloned, in the top level of the repo run the following docker-compose command via the command line to build and run the docker container:\
```docker-compose up --build```

4. Verify the microservice is running. Open a web browser and navigate to the address below:\
```http://localhost:8000/graphql```

## Tests
To run testsuite run `pytest --cov --cov-report=html` to show unit test coverage in an html format.
