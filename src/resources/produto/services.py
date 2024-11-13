from src.resources.produto.models import Produto
from src.resources.produto.schema import ProdutoCreate, ProdutoUpdate
from sqlalchemy.orm import Session

class ProdutoService:

    @staticmethod
    async def create_produto(produto_data: ProdutoCreate, db: Session):
        produto = Produto(**produto_data.dict())
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    @staticmethod
    async def get_produto(produto_id: str, db: Session): 
        return db.query(Produto).filter(Produto.id == produto_id).first()
    
    @staticmethod
    async def get_all_produto(db: Session):
        return db.query(Produto).all()  

    @staticmethod
    async def update_produto(produto_id: str, produto_data: ProdutoUpdate, db: Session): 
        produto = db.query(Produto).filter(Produto.id == produto_id).first()
        if produto:
            for key, value in produto_data.dict(exclude_unset=True).items():
                setattr(produto, key, value)
            db.commit()
            db.refresh(produto)
            return produto
        return None

    @staticmethod
    async def delete_produto(produto_id: str, db: Session):  
        produto = db.query(Produto).filter(Produto.id == produto_id).first()
        if produto:
            db.delete(produto)
            db.commit()
            return True
        return False
