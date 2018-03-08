import datetime
import pymysql


class DBHelper:

    def connect(self, database="mydata"):
        print "Getting connection"
        return pymysql.connect(host='localhost',
                               user="root",
                               passwd="Admin2000",
                               db=database)
       

    def get_data(self):
        connection = self.connect()
        try:
            query = "SELECT country,year,flow,trade FROM data;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            data = []
            for row in cursor:
                datapiece = {
                    'country': row[0].decode('utf8'),
                    'year': row[1].decode('utf8'),
                    'flow': row[2].decode('utf8'),
                    'trade': row[3].decode('utf8')
                }
                data.append(datapiece)
            return data
        finally:
	    connection.close()
