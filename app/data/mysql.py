import pymysql

def update_db(recommendations):
    connection = pymysql.connect(host='db',
                                user='www',
                                password='$3cureUS',
                                db='cs4501',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "TRUNCATE TABLE project2_spark_entries "
            cursor.execute(sql)

            for item in recommendations:
                sql = "INSERT INTO project2_spark_entries (item_id, recommended_items) VALUES (%s, %s)"
                cursor.execute(sql, (item[0], item[1]))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()

