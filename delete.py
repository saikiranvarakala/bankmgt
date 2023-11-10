# installed library mysql-connector-python
import mysql.connector


#creating connection
class delete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",
            password='root',
            database="bank"
        )
    def data_delete(self,table_name,column_name,id):
        cor=self.connection.cursor()
        cor.execute(f"delete from {table_name} where {column_name}={id}")
        self.connection.commit()
        print('-----data is deleted------')