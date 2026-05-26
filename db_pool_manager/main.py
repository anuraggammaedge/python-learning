from enum import Enum
from db_expection import ConnectionFailedError, MaxRetriesExceededError, QueryTimeoutError
import datetime
import random

class Status(Enum):
    ACTIVE = 'active'
    IDLE = 'idle'
    CLOSED = 'closed'


class DatabaseConnection:
    def __init__(self, connection_id):
        self.connection_id = connection_id
        self.status = Status.IDLE
        self.created_at = datetime.datetime.now()

    def connect(self):
        # if random.random() < 0.2:
        #     raise ConnectionFailedError(f"Connection {self.connection_id} failed.")
        self.status = Status.ACTIVE
        print(f"Database connected Successfully. Status: {self.status}")

    def disconnect(self):
        self.status = Status.CLOSED
        print(f"Database Disconnnected Status: {self.status}")

    def execute_query(self, query):
        execution_time = random.randint(1, 10)

        if execution_time > 5:
            raise QueryTimeoutError(f"Query Timeout on connection {self.connection_id}.", 5)
        print(f"Executing: {query}")

    def is_alive(self):
        return self.status == Status.ACTIVE


class ConnectionPool:
    def __init__(self):
        self.max_db_connections = 5
        self.connections = []

    # get available connection or create new one
    def get_connection(self):
        for connection in self.connections:
            try:
                if connection.status == Status.IDLE:
                    connection.connect()
                    return connection
            except Exception as e:
                    raise ConnectionFailedError(str(e))
                
        if len(self.connections) < self.max_db_connections:
            connection_id = len(self.connections) + 1
            new_connection = DatabaseConnection(connection_id)
            new_connection.connect()
            self.connections.append(new_connection)
            print(f"New connection {connection_id} created and added to pool.") 
            return new_connection
        else:
            raise MaxRetriesExceededError(5)

    # return connection to pool
    def release_connection(self, connection):
        if connection in self.connections:
            if connection.status == Status.ACTIVE:
                connection.status = Status.IDLE
                print(f"Connection {connection.connection_id} released to pool")

    # close all connections
    def close_all(self):
        for connection in self.connections:
            connection.disconnect()
        self.connections.clear()

    # return pool statistics
    def get_stats(self):
        total_connections = len(self.connections)
        active_connections = sum(
        1 for conn in self.connections
        if conn.status == Status.ACTIVE
        )

        idle_connections = sum(
            1 for conn in self.connections
            if conn.status == Status.IDLE
        )

        closed_connections = sum(
            1 for conn in self.connections
            if conn.status == Status.CLOSED
        )

        return {
            "total_connections": total_connections,
            "active_connections": active_connections,
            "idle_connections": idle_connections,
            "closed_connections": closed_connections,
            "max_connections": self.max_db_connections
        }



ConnectionPool = ConnectionPool()
try:    
    conn1 = ConnectionPool.get_connection()
    conn2 = ConnectionPool.get_connection()
    conn3 = ConnectionPool.get_connection()
    conn4 = ConnectionPool.get_connection()
    conn5 = ConnectionPool.get_connection()
    # This will raise MaxRetriesExceededError
    conn6 = ConnectionPool.get_connection()

except ConnectionFailedError as e:
    print(f"Connection Failed")
except MaxRetriesExceededError as e:
    print(f"Max Retries Exceeded: ")
except QueryTimeoutError as e:
    print(f"Query Timeout:")

print(ConnectionPool.get_stats())
