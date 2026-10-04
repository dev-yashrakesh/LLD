# class MySQLDatabase:
#
#     def save_order(self, order):
#         return f"Saving order {order} in MySQL"
#
# class OrderService:
#
#     def __init__(self):
#         self.database = MySQLDatabase()
#
#     def create_order(self, order):
#         return self.database.save_order(order)

class DataBaseConnection:
    def save(self):
        pass

class MySQLDataBase(DataBaseConnection):
    def save(self):
        return "saved data to mysql"

class PostSQLDataBase(DataBaseConnection):
    def save(self):
        return "saved data to postsql"

class OrderService:
    def __init__(self, database : DataBaseConnection):
        self.database = database

    def save_data(self):
        return self.database.save()