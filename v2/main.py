from src import app
from flask import request, jsonify
from ariadne import (
    make_executable_schema, 
    graphql_sync, 
    snake_case_fallback_resolvers,
    ObjectType
)
from ariadne.constants import PLAYGROUND_HTML

from src.modules.resolvers import Query, Mutation
from src.modules.typeDefs import type_defs

query = ObjectType("Query")
mutation = ObjectType("Mutation")

for q_name, q_function in Query.items():
    query.set_field(q_name, q_function)

for m_name, m_function in Mutation.items():
   mutation.set_field(m_name, m_function)

schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)

@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=['POST'])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400

    return jsonify(result), status_code