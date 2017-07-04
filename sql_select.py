import mysql.connector
from mysql.connector import errorcode
import time

query_dict = {
    "select_all" : "SELECT * FROM table1",
    "select_by_id" : "SELECT id FROM table1 WHERE id = {0}",
    "select_by_name" : "SELECT name FROM table1 WHERE name LIKE '{0}'"
}

def commonSelect (query):
    returnvalue = None
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='database')
        cursor = cnx.cursor()

        cursor.execute(query)

        returnvalue = list()
        for line in cursor:
            returnvalue.append(line)

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return returnvalue

def selectAll():
    return commonSelect(query_dict["select_all"])

def selectByID(id):
    return commonSelect(query_dict["select_by_id"].format(id))

def selectByNAME(name):
    return commonSelect(query_dict["select_by_name"].format(name))

print selectAll()

