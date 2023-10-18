# Import required modules for a simple HTTP server and for database operations
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base

# Declare the base class for SQLAlchemy declarative models
Base = declarative_base()


# Define the User model for SQLAlchemy
class User(Base):
    """
    SQLAlchemy Model for User.

    Represents a user with an ID, name, and age.
    """

    # Name of the table in the database
    __tablename__ = 'users'

    # Define columns for the user table
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)  # An ID column that auto-increments
    name = Column(String(50))  # A column for user names up to 50 characters
    age = Column(Integer)  # A column for user age as an integer


# Create an SQLite database engine and table if it doesn't exist
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)


# Define the HTTP server request handler
class RequestHandler(SimpleHTTPRequestHandler):
    """
    Request handler for a simple HTTP server.

    Handles POST requests to create a new user.
    """

    def do_POST(self):
        """
        Handle POST requests.
        """
        # Get the content length from the headers to read the correct amount of data
        content_length = int(self.headers['Content-Length'])
        # Read the request body
        body = self.rfile.read(content_length)
        # Convert the request body from JSON format to a Python dictionary
        data = json.loads(body)

        # If the POST request is to the path "/create_user", create a new user
        if self.path == "/create_user":
            # Start a new session with the database
            session = Session()
            # Create a new User instance with data from the request body
            new_user = User(name=data['name'], age=data['age'])
            # Add the new user to the session
            session.add(new_user)
            # Commit changes to the database
            session.commit()
            # Close the session
            session.close()

            # Send a 201 Created response
            self.send_response(201)
            self.end_headers()
            # Send a success message back to the client
            self.wfile.write(b"User created successfully!")
        else:
            # If the request path is not recognized, send a 404 Not Found response
            self.send_response(404)
            self.end_headers()


# Entry point for the script
if __name__ == "__main__":
    # Define the server address and port
    server_address = ('', 8000)
    # Create the HTTP server instance
    httpd = HTTPServer(server_address, RequestHandler)
    # Print a message to indicate the server is running
    print("Server started at http://localhost:8000")
    # Start the server and wait for incoming requests
    httpd.serve_forever()
