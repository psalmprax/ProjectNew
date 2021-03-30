import requests
from utils import set_logger, current_milli_time


LOGGER = set_logger("repository_logger")


class Publisher:
<<<<<<< HEAD
    def get_json_api(self, page):
        get_request = requests.get(page)
        # print(get_request.json())
=======

    def __init__(self):
        pass

    def get_json_api(self, page):
        get_request = requests.get(page)
>>>>>>> fc11ffd78bbf228242c3706ac834c799f83ca9a7
        assert get_request.status_code == 200, "Request not successful"
        return get_request.json(), get_request.status_code

    def apiCall(self, data):
        try:
            return {
                "id": data.get("id"),
                "first_name": data.get("first_name"),
                "last_name": data.get("last_name"),
                "email": data.get("email"),
<<<<<<< HEAD
                "ip_address": data.get("ip_address"),
=======
                "gender": data.get("gender"),
>>>>>>> fc11ffd78bbf228242c3706ac834c799f83ca9a7
                "ip_address": data.get("ip_address"),
                "date": data.get("date"),
                "country": data.get("country"),
                "timestamp_logger": current_milli_time()
            }
            # In the API milliseconds are used.
        except Exception as e:
            LOGGER.info(
                f"Exception: {e}")
            return {}

    def get_all_data_with_model(self, data):
        data_with_model = []
        for line in data:
            data_with_model_temp = self.apiCall(line)
            data_with_model.append(data_with_model_temp)
        return data_with_model
