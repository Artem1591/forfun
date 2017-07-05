import mysql.connector
from mysql.connector import errorcode
import time


def summ(data):
    return "{0}+{1}={2}".format((data[1]),(data[2]),(data[1])+ (data[2]))

def test(data):
    print "got data {0}".format(data)
    return data

math_dict = {
        "sum": summ,
        "test": test
    }



#if __name__ == '__main__':
 #   import  argparse
 #   parser = argparse.ArgumentParser(description='HTTP Server')
  #  parser.add_argument('id', type=int, help='database id')
   # args = parser.parse_args()
    #insertData(name = args.id)


#print selectByID(args.id)