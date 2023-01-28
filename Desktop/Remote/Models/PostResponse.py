from Desktop.Remote.Models.Post import Post


class PostResponse:

    def __init__(self, error, message, data):
        self.data = data
        self.message = message
        self.error = error

    def toPost(self):
        return Post(
            self.data['id'],
            self.data['post_title'],
            self.data['post_description'],
        )

    def toList(self):
        List_post = []
        for i in self.data:
            List_post.append(
                Post(id=i["id"], title=i["post_title"], description=i["post_description"])
            )
        return List_post
