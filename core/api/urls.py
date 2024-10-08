from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI

from core.api.schemas import PingResponseSchema
from core.api.v1.urls import router as v1_router


api = NinjaAPI(title='Boilerplate')

api.add_router('v1/', v1_router)


@api.get("/ping", response=PingResponseSchema)
def ping(request: HttpRequest):
    return {"result": True}


urlpatterns = [
    path("", api.urls),
]
