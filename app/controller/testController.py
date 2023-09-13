from fastapi import APIRouter, HTTPException
from ..service import testService
from ..schema.testSchema import PostTestSchema

router = APIRouter(
    prefix="/test",
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def index_test():
    return testService.index_test()

@router.get("/{id}")
async def get_test(id:int):
    try:
        return testService.get_test(id)
    except:
        raise HTTPException(status_code=404)
    
@router.post("/")
async def creste_test(test: PostTestSchema):
    return testService.create_test(test)