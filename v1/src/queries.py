from src.models import Post
from ariadne import convert_kwargs_to_snake_case

def listPosts_resolver(obj, info):
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
def getPost_resolver(obj, info, id):
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

