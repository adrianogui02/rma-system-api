from sqlalchemy.orm import Session
from src.resources.produto.models import Produto
from src.resources.produto.schema import ProdutoCreate, ProdutoUpdate

class ProdutoService:

    @staticmethod
    async def create_produto(produto_data: ProdutoCreate, db: Session, usuario_id: str):
        produto = Produto(**produto_data.dict(), usuario_id=usuario_id)
        db.add(produto)
        db.commit()
        db.refresh(produto)
        return produto

    @staticmethod
    async def get_produto(produto_id: str, db: Session, usuario_id: str): 
        return db.query(Produto).filter(Produto.id == produto_id, Produto.usuario_id == usuario_id).first()
    
    @staticmethod
    async def get_all_produto(db: Session, usuario_id: str):
        return db.query(Produto).filter(Produto.usuario_id == usuario_id).all()
    
    @staticmethod
    async def get_all(db: Session):
        produtos = db.query(Produto).all()
        print(produtos)  # Isso vai te ajudar a ver o que está sendo retornado
        return produtos

    @staticmethod
    async def update_produto(produto_id: str, produto_data: ProdutoUpdate, db: Session, usuario_id: str): 
        produto = db.query(Produto).filter(Produto.id == produto_id, Produto.usuario_id == usuario_id).first()
        if produto:
            for key, value in produto_data.dict(exclude_unset=True).items():
                setattr(produto, key, value)
            db.commit()
            db.refresh(produto)
            return produto
        return None

    @staticmethod
    async def delete_produto(produto_id: str, db: Session, usuario_id: str):  
        produto = db.query(Produto).filter(Produto.id == produto_id, Produto.usuario_id == usuario_id).first()
        if produto:
            db.delete(produto)
            db.commit()
            return True
        return False
