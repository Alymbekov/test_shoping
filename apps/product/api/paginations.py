from rest_framework.pagination import LimitOffsetPagination


class CustomOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 500

    # def get_paginated_response(self, data):
