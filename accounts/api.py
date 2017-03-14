# coding: utf-8
from django.http import JsonResponse
from rest_framework import decorators
from oauth2_provider.decorators import protected_resource


@decorators.api_view(['POST', 'GET', ])
@protected_resource()
def profile(request):
    user = request.resource_owner

    # User Info Response
    data = {
        'user_id': user.id,
        'email': user.email,
        'date_joined': user.date_joined,
        'secret_message': 'This is a test.',
        'endpoint_name': 'accounts.api.profile',
    }
    return JsonResponse(data)
