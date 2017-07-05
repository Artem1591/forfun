import mysql.connector
from mysql.connector import errorcode

query_dict = {
    "delete_id" : "DELETE FROM `database`.`table1` WHERE idtable1 = ({0});",
}

def commonDelete(query):
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

def deleteID(id):
    return commonDelete(query_dict["delete_id"].format(id))

#print deleteID(3)

