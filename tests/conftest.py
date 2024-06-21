import pytest
from ..src.app import create_app
from ..src.model.database import Base, engine, Session


# Use the scope = module because fixtures should be set up once per each Python file containing tests
@pytest.fixture(scope="module")
def app():
    # Create a new app instance for each test module
    application = create_app()

    # Configure Flask app for testing with an in-memory SQLite database
    # Put Flask into testing mode
    application.config['TESTING'] = True
    # Use an in-memory SQLite database for tests
    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    # Event system is not needed
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Set Flask into production mode by disabling debug mode (it affects error handling)
    application.config['DEBUG'] = False

    # Create the database schema
    with application.app_context():
        Base.metadata.create_all()

    yield application

    # After test are done, drop everything
    with application.app_context():
        Base.metadata.drop_all()


# Use the scope = function (it will be recreated for each test function)
@pytest.fixture(scope="function")
def client(app):
    # Include a test client to simulate the testing
    return app.test_client()


@pytest.fixture(scope="function")
def session(app):
    # Start a transaction for testing
    connection = engine.connect()
    transaction = connection.begin()

    # Create a session using the connection
    session = Session(bind=connection)

    yield session

    # Close the session, rollback, and close the connection
    session.close()
    transaction.rollback()
    connection.close()
