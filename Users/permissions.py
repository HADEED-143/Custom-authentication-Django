from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User
"""class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET', 'PUT']
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user"""

class isEmployerUser(BasePermission):
    message = 'You must be a client to access this page.'
    def has_permission(self, request, view):
        if request.user.is_client:
            return True
        return False
class isLaborerUser(BasePermission):
    message = 'You must be a laborer to access this page.'
    def has_permission(self, request, view):
        if request.user.is_laborer:
            return True
        return False
class ContractorUser(BasePermission):
    message = 'You must be a contractor to access this page.'
    def has_permission(self, request, view):
        if request.user.is_contractor:
            return True
        return False


class IsAuthenticated:
    pass