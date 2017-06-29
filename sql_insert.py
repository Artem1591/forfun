import mysql.connector
from mysql.connector import errorcode
import time

query_dict = {
    "insert_id" : "INSERT INTO `database`.`table1`(`idtable1`) VALUES ({0});",
    "insert_name" : "INSERT INTO `database`.`table1`(`name`) VALUES ('{0}');"
}

def commonInsert(query):
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='database')
        cursor = cnx.cursor()

        cursor.execute(query)

        cnx.commit()

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def insertID(id):
    return commonInsert(query_dict["insert_id"].format(id))

def insertName(name):
    return commonInsert(query_dict["insert_name"].format(name))

print insertID(3)
print insertName('Vazgen')
