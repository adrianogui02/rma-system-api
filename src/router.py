# router.py
from fastapi import APIRouter
from src.resources.auth.controller import router as auth_router
from src.resources.rma.controller import router as rma_router
from src.resources.produto.controller import router as produto_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(rma_router, prefix="/rma", tags=["RMA"])
router.include_router(produto_router, prefix="/produto", tags=["Produto"])