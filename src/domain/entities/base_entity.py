from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
