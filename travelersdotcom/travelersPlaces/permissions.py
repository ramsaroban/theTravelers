from django.contrib.auth import get_user_model
Users = get_user_model()

from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404


class PlacePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            else:
                return False
        else:
        	user=get_object_or_404(Users,id=request.user.id)
        	if request.method in SAFE_METHODS:
        		return True
        	else:
        		if user.is_staff or user.is_superuser or user.is_admin:
        			return True
        		else:
        			return False