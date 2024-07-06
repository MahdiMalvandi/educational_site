from rest_framework.permissions import BasePermission


class TeacherOrAdmins(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_staff or request.user.is_superuser or request.user.is_teacher:
                return True
            else:
                return False
        except:
            return False


class OnlySuperUser(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_superuser:
                return True
            else:
                return False
        except:
            return False
