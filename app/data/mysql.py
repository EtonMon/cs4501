import MySQLdb

def update_db(recommendations):
    connection = MySQLdb.connect(host='db',
                                user='www',
                                passwd='$3cureUS',
                                db='cs4501')
    try:
        cursor = connection.cursor()
        # Create a new record
        sql = "TRUNCATE TABLE project2_spark_entries"
        cursor.execute(sql)

        for item in recommendations:
            sql = "INSERT INTO project2_spark_entries (item_id, recommended_items) VALUES (%s, %s)"
            cursor.execute(sql, (str(item[0]), str(item[1])))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()

