from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def createConnection(host, user, password, databaseName):
    connection = QSqlDatabase.addDatabase("QMYSQL")
    connection.setHostName(host)
    connection.setUserName(user)
    connection.setPassword(password)
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True

def _createContactsTable():
    createTableQr = QSqlQuery()
    return createTableQr.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

# Example usage:
if __name__ == "__main__":
    if createConnection("localhost", "username", "password", "contacts_db"):
        print("Database connected and table created.")
    else:
        print("Failed to connect to the database.")
