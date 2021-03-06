from rest_framework import permissions
from user.models import User


class IsUpdateProfile(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own profile
    """
    def has_permission(self, request, view):

        if request.user.is_staff:
            return True
        # print(view.kwargs)
        # print(request.user.id)
        # Look for the requested user in the database
        try:
            user_profile = User.objects.get(
                pk=view.kwargs['pk'])
        except:
            # If the user was not found then return false
            return False

        # Check that the requesting user id matches the authenticated user id
        # print(request.user)
        # print(user_profile)
        if request.user == user_profile:
            return True
        return False


class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user

