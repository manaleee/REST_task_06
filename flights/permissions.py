from rest_framework.permissions import BasePermission

# from datetime import datetime
from datetime import date




class OwnerOrStaff(BasePermission):
	message = "only owners & staff have access"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or request.user == obj.user:
			return True
		return False
		





class BookingOnly(BasePermission):
	message = "NO time"
	

	def has_object_permission(self, request, view, obj):
		day_left = (obj.date - date.today()).days

		if day_left > 3:
			return True
		return False	
