from rest_framework.exceptions import APIException


class EventDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested event does not exist.'