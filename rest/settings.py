INSTALLED_APPS = (
""" 
"""
	'rest_framework',
	)

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
	'PAGINATE_BY': 10
}
