import logging

logger = logging.getLogger(__name__)


class OperationLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            logger.info('%s %s %s', request.user.username, request.method, request.path)
        return response
