from src.infrastructure.configurations.config import Base, engine

Base.metadata.create_all(bind=engine)
