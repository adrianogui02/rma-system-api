from fastapi import APIRouter, HTTPException, Depends
from src.resources.produto.services import ProdutoService
from src.resources.produto.schema import ProdutoCreate, ProdutoUpdate, Produto
from src.database.database import SessionLocal
from sqlalchemy.orm import Session


router = APIRouter()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Produto])
async def get_all_product(db: Session = Depends(get_db)):
    produtos = await ProdutoService.get_all_produto(db)
    return produtos

@router.post("/", response_model=Produto)
async def create_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return await ProdutoService.create_produto(produto, db)

@router.get("/{produto_id}", response_model=Produto)
async def read_produto(produto_id: str, db: Session = Depends(get_db)):  
    produto = await ProdutoService.get_produto(produto_id, db)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{produto_id}", response_model=Produto)
async def update_produto(produto_id: str, produto: ProdutoUpdate, db: Session = Depends(get_db)):  
    updated_produto = await ProdutoService.update_produto(produto_id, produto, db)
    if not updated_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_produto

@router.delete("/{produto_id}", status_code=204)
async def delete_produto(produto_id: str, db: Session = Depends(get_db)):  
    success = await ProdutoService.delete_produto(produto_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"message": "Produto excluído com sucesso"}
