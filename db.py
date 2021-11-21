import psycopg2

#connection to db
def connect():
    con = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "postgres",
        database = "ecommerce"
    )
    cur = con.cursor()
    return con, cur

def getProducts():
    con, cur = connect()
    # cur = con.cursor()
    # cur.execute("SELECT * FROM products LIMIT 10")
    cur.execute("SELECT title, COUNT(id) as total, SUM(price) as total_amount FROM products GROUP BY title HAVING title ILIKE 'A%'")
    con.commit()
    #get rows
    rows = cur.fetchall()
    print("Title   Total    Total Price")
    for r in rows:
        print(r[0] + "  " + str(r[1]) + "   " + str(r[2]))

getProducts()


def getUsers():
    con, cur = connect()
    # cur.execute("SELECT * FROM users LIMIT 5")
    # cur.execute("SELECT name, registration_date, AGE(NOW(), registration_date) as time_passed FROM users limit 5")
    cur.execute("SELECT name, registration_date FROM users WHERE registration_date BETWEEN NOW() - INTERVAL '1 MONTH' AND NOW() limit 5")
    rows = cur.fetchall()

    for row in rows:
        # print(row[1]+ " " + row[2] + " " +str(row[3]))
        # print(f"{row[1]} {row[2]} {row[3]}")
        # print(f"{row[0]} {row[1]} {row[2]}")

        print(f"{row[0]} {row[1]}")

        cur.close()
        con.close()

       

getUsers()