# # authentication_middleware.py

# from django.shortcuts import redirect
# from django.urls import reverse

# # List of views that don't require authentication
# EXEMPT_VIEWS = ['register', 'login','check_email_exists']

# class CustomAuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             response = self.get_response(request)
#             return response

#         if request.resolver_match and request.resolver_match.url_name not in EXEMPT_VIEWS:
#             return redirect(reverse('login'))  # Adjust the URL name for your login view

#         response = self.get_response(request)
#         return response
