from sqlmodel import SQLModel, create_engine, Session, select
#from models import Asset
engine = create_engine("postgresql://root:password@localhost:5432/kala")
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
# commented code below is to check if the database is connected properly 
# def get_assets():
#     with Session(engine) as session:
#         statement = select(Asset)
#         results = session.exec(statement)
#         return results.all()
# assets = get_assets()

# assets_types = [asset.type for asset in assets]
# assets_balances = [asset.balance for asset in assets]
# print(assets_types)
# print(assets_balances)