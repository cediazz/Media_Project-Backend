from rest_framework.routers import DefaultRouter
from .views import CategoryView,PlanView,CoordinadasView,MediaFieldView,MediaView

router = DefaultRouter()
router.register(r'Categorys',CategoryView)
router.register(r'Plans',PlanView)
router.register(r'Coordinadas',CoordinadasView)
router.register(r'Media',MediaView)
router.register(r'Media-field',MediaFieldView)
urlpatterns = router.urls