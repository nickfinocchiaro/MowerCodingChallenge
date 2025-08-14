"""Robomower GraphQL Simulator
Sets up a FastAPI application with a GraphQL endpoint for the Robotic Lawnmower Simulator.
It includes the GraphQL schema and routes for handling simulation requests.
It uses Strawberry for GraphQL integration with FastAPI.
"""
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from lawnmower.graphql_schema import Query

schema = strawberry.Schema(query=Query)
lawnmower_graphql_app = GraphQLRouter(schema)

lawnmower_app = FastAPI(title="Robomower GraphQL Simulator")
lawnmower_app.include_router(lawnmower_graphql_app, prefix="/graphql")
