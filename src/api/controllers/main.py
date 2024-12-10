from src.infrastructure.configurations.database import Base, engine

Base.metadata.create_all(bind=engine)
