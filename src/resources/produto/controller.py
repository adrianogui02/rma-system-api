from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.resources.produto.services import ProdutoService
from src.resources.produto.schema import ProdutoCreate, ProdutoUpdate, Produto
from src.database.database import SessionLocal
from src.resources.rma.dependencies import get_user_id 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Produto])
async def get_all_produto(db: Session = Depends(get_db), usuario_id: str = Depends(get_user_id)):
    produtos = await ProdutoService.get_all_produto(db, usuario_id)
    return produtos

@router.post("/", response_model=Produto)
async def create_produto(produto: ProdutoCreate, db: Session = Depends(get_db), usuario_id: str = Depends(get_user_id)):
    return await ProdutoService.create_produto(produto, db, usuario_id)

@router.get("/{produto_id}", response_model=Produto)
async def read_produto(produto_id: str, db: Session = Depends(get_db), usuario_id: str = Depends(get_user_id)):  
    produto = await ProdutoService.get_produto(produto_id, db, usuario_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{produto_id}", response_model=Produto)
async def update_produto(produto_id: str, produto: ProdutoUpdate, db: Session = Depends(get_db), usuario_id: str = Depends(get_user_id)):  
    updated_produto = await ProdutoService.update_produto(produto_id, produto, db, usuario_id)
    if not updated_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_produto

@router.delete("/{produto_id}", status_code=204)
async def delete_produto(produto_id: str, db: Session = Depends(get_db), usuario_id: str = Depends(get_user_id)):  
    success = await ProdutoService.delete_produto(produto_id, db, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"message": "Produto excluído com sucesso"}

@router.get("/all/get", response_model=list[Produto])
async def get_all(db: Session = Depends(get_db)):
    produtos = await ProdutoService.get_all(db)
    return produtos