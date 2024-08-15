from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1711999@host.docker.internal:33061/StreamETL_DB")

meta = MetaData()