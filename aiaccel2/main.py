from fastapi import FastAPI

from aiaccel2.user.presentation.api.v1.health import health_router
from aiaccel2.user.presentation.api.v1.user.create_one_router import create_one_router
from aiaccel2.user.presentation.api.v1.user.delete_one_router import delete_one_router
from aiaccel2.user.presentation.api.v1.user.find_all_router import find_all_router
from aiaccel2.user.presentation.api.v1.user.find_one_router import find_one_router
from aiaccel2.user.presentation.api.v1.user.update_one_router import update_one_router

app = FastAPI()

app.include_router(health_router)
app.include_router(find_all_router)
app.include_router(find_one_router)
app.include_router(create_one_router)
app.include_router(delete_one_router)
app.include_router(update_one_router)
