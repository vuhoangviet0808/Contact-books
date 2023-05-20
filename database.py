from PyQt6.QtWidgets import QMessageBox

from PyQt6.QtSql import QSqlDatabase,QSqlQuery

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            QMessageBox.StandardButton,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _creatContactsTable()
    return True


def _creatContactsTable():
    creattableQr = QSqlQuery()
    return creattableQr.exec(
        """
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name VARCHAR(40) NOT NULL,
                    job VARCHAR(50),
                    email VARCHAR(40) NOT NULL
                )
                """
    )