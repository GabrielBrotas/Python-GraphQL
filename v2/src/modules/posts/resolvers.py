from src.modules.posts.models.Post import Post
from ariadne import convert_kwargs_to_snake_case
from datetime import date
from src import db

def query_list_posts(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        payload = {
            "success": True,
            "posts": posts
        }
        
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


@convert_kwargs_to_snake_case #This decorator converts the method arguments from camel case to snake case
def query_get_post(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def mutation_create_post(obj, info, title, description):
    try:
        today = date.today()
        print(today)
        post = Post(
            title=title, description=description, created_at=today
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def mutation_update_post(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def mutation_delete_post(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

Query = {
    "listPosts": query_list_posts,
    "getPost": query_get_post
}

Mutation = {
    "createPost": mutation_create_post,
    "updatePost": mutation_update_post,
    "deletePost": mutation_delete_post
}