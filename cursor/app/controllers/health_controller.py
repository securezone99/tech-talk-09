from fastapi import APIRouter

router = APIRouter()
router = APIRouter(tags=["health-api"])

@router.get("/ready")
async def ready():
    return {"message": "Recommender is ready to process requests"}

@router.get("/live")
async def live():
    return {"message": "Recommender is live"}