from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from lawnmower.graphql_schema import Query
import strawberry

schema = strawberry.Schema(query=Query)
lawnmower_graphql_app = GraphQLRouter(schema)

lawnmower_app = FastAPI(title="Robomower GraphQL Simulator")
lawnmower_app.include_router(lawnmower_graphql_app, prefix="/graphql")