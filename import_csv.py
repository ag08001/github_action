import pandas as pd
import pandas as pd
import os
import cx_Oracle
import sqlalchemy
from sqlalchemy import Column, String, create_engine

os.environ["LD_LIBRARY_PATH"]="/Users/mac/opt/oracle/instantclient_19_8"
os.environ["ORACLE_HOME"]="/Users/mac/opt/oracle/instantclient_19_8"
a = pd.read_csv('/Users/mac/Downloads/IF9999_CCFX.csv',encoding='utf-8',header=0).astype({'date':str,'time':str})
a.rename(columns={'date': 'dates'}, inplace=True)
oraengine = create_engine('oracle+cx_oracle://data:data@192.168.165.160:1521/orcl', echo=True)
pd.io.sql.to_sql(a, 'if9999', oraengine.connect(), if_exists='append', index=False, )
print(a.head())