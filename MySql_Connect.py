import mysql.connector
#print(mysql.connector.__version__)
# Connect to the local MySQL database
try:
    conn = mysql.connector.connect(
        host="193.203.184.6",
        user="u547203012_alagarusr",
        password="Yayaya@143",
        database="u547203012_alagardb")
    print(mysql.connector.__version__)
    cursor = conn.cursor()
    cursor.execute("SELECT Revenue FROM Balance_Sheet where Revenue>10000")
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matching rows found.")
except mysql.connector.Error as err:
    print("Database error:", err)
except Exception as e:
    print("Unexpected error:", e)
finally:
    if conn.is_connected():
       print("Connected")
    #  conn.close()