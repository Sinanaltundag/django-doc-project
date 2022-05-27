from .views import DetailView, IndexView, ResultsView, detail, results, vote
from django.urls import  path

from polls.views import index

app_name= "polls" # hreflerde verilen "url" nin hangi app i çağıracağını belirtir
urlpatterns = [
    # path("", index),
    # path("<int:question_id>/", detail, name="detail"),
    # path("<int:question_id>/results", results, name="results"),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote", vote, name="vote"),

]