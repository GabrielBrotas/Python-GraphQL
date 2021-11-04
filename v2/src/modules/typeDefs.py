type_defs = """"""

with open("./src/modules/posts/schema.graphql", "r") as file:
    # we are going to execute some code and after this we close this file
    r = file.read()
    type_defs += r
