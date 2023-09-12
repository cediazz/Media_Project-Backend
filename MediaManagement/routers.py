from rest_framework.routers import DefaultRouter
from .views import CategoryView,PlanView,CoordinadasView,MediaView,FieldView,MediaContainerView,Media_FieldView

router = DefaultRouter()
router.register(r'Categorys',CategoryView)
router.register(r'Plans',PlanView)
router.register(r'Coordinadas',CoordinadasView)
router.register(r'Fields',FieldView)
router.register(r'Media',MediaView)
router.register(r'Media-Field',Media_FieldView)
router.register(r'MediaContainer',MediaContainerView)
urlpatterns = router.urls