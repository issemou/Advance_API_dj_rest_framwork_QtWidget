import json
import requests

from Desktop.Remote.Models.PostResponse import PostResponse
from Desktop.Remote.Models.authModel import AuthModel


class HttpClient:
    def authentication(self, username, password, on_complete, on_error, on_faillure):

        try:
            url = "http://127.0.0.1:8000/dj-rest-auth/login/"
            post = {"username": username, "password": password}
            resp = requests.post(url=url, data=post)
            reslt = json.loads(resp.text)
            user = AuthModel(token=reslt['key'])
            if on_complete:
                if user.token:
                    on_complete(user)
        except requests.ConnectionError:
            error = "Connexion au server impossible veuillez reeasyer"
            if on_error:
                on_error(error)
            if on_faillure:
                on_faillure(error)

    def registration(self, email, username, password1, password2, on_complete, on_error, on_faillure):

        try:
            url = "http://127.0.0.1:8000/dj-rest-auth/registration/"
            post = {"username": username,
                    "password1": password1,
                    "password2": password2,
                    "email": email}
            resp = requests.post(url=url, data=post)
            reslt = json.loads(resp.text)
            user = AuthModel(token=reslt['key'])
            if on_complete:
                if user.token:
                    on_complete(user)
        except requests.ConnectionError:
            error = "Connexion au server impossible veuillez reeasyer"
            if on_error:
                on_error(error)
            if on_faillure:
                on_faillure(error)

    def log_out(self, on_complete, on_error, on_faillure):
        try:
            url = "http://127.0.0.1:8000/dj-rest-auth/logout/"
            resp = requests.post(url=url)
            result = json.loads(resp.text)
            user = AuthModel(token=result['key'])
            if on_complete:
                if user.token:
                    on_complete(user)
        except requests.ConnectionError:
            error = "Connexion au server impossible veuillez reeasyer"
            if on_error:
                on_error(error)
            if on_faillure:
                on_faillure(error)

    def get_all_post(self, on_complete, on_error, on_faillure):

        try:
            url = "http://127.0.0.1:8000/api/post_2/"
            data = requests.get(url)
            result = json.loads(data.text)
            r = PostResponse(result['error'], result['message'], result['data'])
            list_post = r.toList()
            if on_complete:
                on_complete(list_post)

        except requests.ConnectionError:

            error = "Connexion au server impossible veuillez reeasyer"

            if on_error:
                on_error(error)

            if on_faillure:
                on_faillure(error)

    def get_post_by_id(self, id, on_complete, on_error, on_faillure):

        try:
            url = f"http://127.0.0.1:8000/api/post_2/{id}/"
            data = requests.get(url)
            result = json.loads(data.text)
            PostResponse(result['error'], result['message'], result['data'])
            post = PostResponse.toPost()
            if on_complete:
                on_complete(post)
        except requests.ConnectionError:

            error = "Connexion au server impossible veuillez reeasyer"

            if on_error:
                on_error(error)

            if on_faillure:
                on_faillure(error)

    def create_post(self, post_title, post_description, on_complete, on_error, on_faillure):
        try:
            url = f"http://127.0.0.1:8000/api/post_2/"
            post = {"post_title": post_title, "post_description": post_description}
            resp = requests.post(url=url, data=post)
            result = json.loads(resp.text)
            r = PostResponse(result['error'], result['message'], None)

            if on_complete:
                on_complete(r.message)

        except requests.ConnectionError:

            error = "Connexion au server impossible veuillez reeasyer"

            if on_error:
                on_error(error)

            if on_faillure:
                on_faillure(error)

    def update_post(self, id, post_title, post_description, on_complete, on_error, on_faillure):

        try:
            url = f"http://127.0.0.1:8000/api/post_2/{id}/"
            post = {"post_title": post_title, "post_description": post_description}
            resp = requests.put(url=url, data=post)
            result = json.loads(resp.text)
            r = PostResponse(result['error'], result['message'], None)

            if on_complete:
                on_complete(r.message)

        except requests.ConnectionError:

            error = "Connexion au server impossible veuillez reeasyer"

            if on_error:
                on_error(error)

            if on_faillure:
                on_faillure(error)

    def delete_post(self, id, on_complete, on_error, on_faillure):

        try:
            url = f"http://127.0.0.1:8000/api/post_2/{id}/"
            resp = requests.delete(url=url)
            result = json.loads(resp.text)
            r = PostResponse(result['error'], result['message'], None)

            if on_complete:
                on_complete(r.message)

        except requests.ConnectionError:

            error = "Connexion au server impossible veuillez reeasyer"

            if on_error:
                on_error(error)

            if on_faillure:
                on_faillure(error)
