from django.http import JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView


class ProfileView(ProtectedResourceView):
    def get(self, request, **kwargs):
        user = request.resource_owner

        # User Info Response
        data = {
            'user_id': user.id,
            'email': user.email,
            'date_joined': user.date_joined,
            'secret_message': 'This is a test.',
        }
        return JsonResponse(data)


profile = ProfileView.as_view()
