from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from lawnmower.graphql_schema import Query
import strawberry

schema = strawberry.Schema(query=Query)
lawnmower_graphql_app = GraphQLRouter(schema)

app = FastAPI(title="Robomower GraphQL Simulator")
app.include_router(lawnmower_graphql_app, prefix="/graphql")