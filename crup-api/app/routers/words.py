from fastapi import APIRouter

router = APIRouter(
     prefix="/words",
    tags=["words"],
)

@router.get("",response_description="List words")
async def get_words(): 
    return {"Words": "fakeword"}