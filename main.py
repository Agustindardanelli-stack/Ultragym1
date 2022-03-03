import pymysql
class Database :
    def __init__ (self):
        self.connection = pymysql.connect(
            host= 'localhost',
            user= 'root',
            password= '43131804Tuti',
            db= 'efi'
        )
        self.cursor = self.connection.cursor()


    print("COnexion establecida")
    def select_user (self,id):
        sql = ' SELECT id , username , email FROM users WHere id = {}'.format(id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()            
            print("id",user[0])
            print("username",user[1])
            print("email",user[2])
        except Exception as e :
            raise    


database = Database
database.select_user ( 1 )

