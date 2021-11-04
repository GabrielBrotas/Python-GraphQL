from src.modules.posts.resolvers import Query as PostQuery, Mutation as PostMutation

Query = {
    **PostQuery,
}

Mutation = {
    **PostMutation,
}