from src.infrastructure.config import Base, engine

Base.metadata.create_all(bind=engine)
