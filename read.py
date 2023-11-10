# installed library mysql-connector-python
import mysql.connector


#creating connection
class read:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",
            password='root',
            database="bank"
        )

    def specific_info(self,ID,table_name,column_name):
        cur=self.connection.cursor()
        cur.execute(f"select * from {table_name} where {column_name}={ID}")
        print(cur.fetchall())
