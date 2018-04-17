from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        user = request.user

        if path == '/admin/':
            return None
        elif user.is_authenticated and any(url == path for url in settings.LOGIN_EXEMPT_URLS):
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif not user.is_authenticated and not any(url == path for url in settings.LOGIN_EXEMPT_URLS):
            print(path, "matched", end="\n")
            return redirect(settings.LOGIN_URL)


class RedirectionToIndexMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info
        if path == '':
            return redirect('/todoapp/')


"""
import inspect to see the source code of a function object
inspect.getsource(function)
"""
