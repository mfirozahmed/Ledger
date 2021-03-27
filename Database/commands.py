def getProductSQL(database):
    sql = ("SELECT * FROM products WHERE status ='1'")
    database.cursor.execute(sql)
    result = database.cursor.fetchall()
    return result



def addProductSQL(product, database):
    sql = ("INSERT INTO products(name, buyPrice, sellPrice, profit, quantity, status) VALUES (%s, %s, %s, %s, %s, %s)")
    database.cursor.execute(sql, (product['name'], product['buyPrice'], product['sellPrice'], product['profit'], product['quantity'], product['status']))
    database.db.commit()



def deleteProductSQL(product, database):
    sql = ("UPDATE products SET status = %s WHERE name = %s")
    database.cursor.execute(sql, (0, product['name'],))
    database.db.commit()



def buyProductSQL(product, database):
    sql = ("UPDATE products SET quantity = %s WHERE name = %s")
    database.cursor.execute(sql, (product['quantity'], product['name'],))
    database.db.commit()

    sql = ("INSERT INTO transections(name, type, quantity) VALUES (%s, %s, %s)")
    database.cursor.execute(sql, (product['name'], "buy", product['quantity'],))
    database.db.commit()



def sellProductSQL(product, database):
    sql = ("UPDATE products SET quantity = %s WHERE name = %s")
    database.cursor.execute(sql, (product['quantity'], product['name'],))
    database.db.commit()

    sql = ("INSERT INTO transections(name, type, quantity) VALUES (%s, %s, %s)")
    database.cursor.execute(sql, (product['name'], "sell", product['quantity'],))
    database.db.commit()






def getBalanceSQL(database):
    sql = ("SELECT * FROM balance ORDER BY created DESC")
    database.cursor.execute(sql)
    result = database.cursor.fetchone()
    return result



def addBalanceSQL(balance, profit, database):
    sql = ("INSERT INTO balance(type, profit, balance) VALUES (%s, %s, %s)")
    database.cursor.execute(sql, ("sell", profit, balance))
    database.db.commit()



def reduceBalanceSQL(balance, value, database):
    sql = ("INSERT INTO balance(type, profit, balance) VALUES (%s, %s, %s)")
    database.cursor.execute(sql, ("buy", value, balance))
    database.db.commit()