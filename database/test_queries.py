from database.connection import get_connection


def get_transaction(transaction_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM transactions
        WHERE transaction_id = %s
    """

    cursor.execute(query, (transaction_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


if __name__ == "__main__":

    result = get_transaction("TX1001")

    print("Transaction:")
    print(result)