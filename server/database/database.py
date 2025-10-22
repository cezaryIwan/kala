from sqlmodel import SQLModel, create_engine, Session

engine = create_engine("postgresql://root:password@db:5432/kala")
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session