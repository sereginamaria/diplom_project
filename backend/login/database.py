import psycopg2

class Data_Base:
    def __init__(self):
        self.connection = False

    def connect(self):
        self.connection = psycopg2.connect(dbname = "education_system",
                                           user = "maria",
                                           password = "maria",
                                           host = "localhost")

    def get_users(self):
        if not(self.connection):
            self.connect()
        cursor = self.connection.cursor()
        response = False
        try:
            sql_request = '''SELECT * FROM users;'''
            cursor.execute(sql_request)
            users = cursor.fetchall()

            response = { "totalElements": len(users), "items": []}
            for user in users:
                items = dict()
                items["user_id"] = user[0]
                items["user_name"] = user[1] + ' ' + user[2]
                items["user_class"] = user[3]
                items["user_school_id"] = user[4]
                response["items"].append(items)
        except:
            print("Ошибка при работе с PostgreSQL")
        cursor.close()
        self.connection.close()
        self.connection = False
        return response

'''
new_tab = Data_Base()
'''







