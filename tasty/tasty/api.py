from rest_framework import routers
from recipes import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'recepies', myapp_views.RecipeViewset)