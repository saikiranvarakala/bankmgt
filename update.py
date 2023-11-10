# installed library mysql-connector-python
import mysql.connector


#creating connection
class update:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",
            password='root',
            database="bank"
        )

    def myupdate(self,table_name,column_name,newvalue,id,column_id):
        cur=self.connection.cursor()
        if newvalue.isnumeric():
            cur.execute(f"update {table_name} set {column_name}={int(newvalue)} where {column_id}={id}")
        else:
            cur.execute(f"update {table_name} set {column_name}='{newvalue}' where {column_id}={id}")
        self.connection.commit()
        print('----info is updated-------')