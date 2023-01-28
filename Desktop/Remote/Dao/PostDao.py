from Desktop.Remote.ApiRemote.Http_client import HttpClient


class PostDao:

    def auth(self, username, password, on_server_data, on_server_error, on_request_faillure):
        HttpClient().authentication(username=username, password=password,
                                    on_complete=on_server_data, on_error=on_server_error,
                                    on_faillure=on_request_faillure)

    def log_out(self, on_server_data, on_server_error, on_request_faillure):
        HttpClient().log_out(on_complete=on_server_data, on_error=on_server_error,
                             on_faillure=on_request_faillure)

    def get_list_post(self, on_server_data, on_server_error, on_request_faillure):
        HttpClient().get_all_post(on_complete=on_server_data, on_error=on_server_error,
                                  on_faillure=on_request_faillure)

    def get_post_by_id(self, id, on_server_data, on_server_error, on_request_faillure):
        HttpClient().get_post_by_id(id=id, on_complete=on_server_data, on_error=on_server_error,
                                    on_faillure=on_request_faillure)

    def create_post(self, title, description, on_server_data, on_server_error, on_request_faillure):
        HttpClient().create_post(post_title=title, post_description=description, on_complete=on_server_data,
                                 on_error=on_server_error,
                                 on_faillure=on_request_faillure)

    def update_post(self, id, title, description, on_server_data, on_server_error, on_request_faillure):
        HttpClient().update_post(id=id, post_title=title, post_description=description, on_complete=on_server_data,
                                 on_error=on_server_error,
                                 on_faillure=on_request_faillure)

    def delete_post(self, id, on_server_data, on_server_error, on_request_faillure):
        HttpClient().delete_post(id=id, on_complete=on_server_data,
                                 on_error=on_server_error,
                                 on_faillure=on_request_faillure)
