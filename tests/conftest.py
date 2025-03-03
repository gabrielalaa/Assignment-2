import pytest
# from src.app import create_app
from src.model.database import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Set up a session for testing the databases
@pytest.fixture(scope="function")
def db_session():
    # Use an in-memory SQLite database
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    # Create a session with autoflush disabled to prevent automatic pre-query flushes which might affect tests
    local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session = local_session()
    try:
        yield session
    # After each test:
    finally:
        # Make sure to close the session
        session.close()
        # Clean up the schema
        Base.metadata.drop_all(engine)


# Use the scope = function (it will be recreated for each test function)
@pytest.fixture(scope="function")
def client(app):
    # Include a test client to simulate the testing
    return app.test_client()


# # Create an engine instance with an in-memory SQLite database
# engine = create_engine('sqlite:///:memory:')
#
#
# # # Use the scope = module because fixtures should be set up once per each Python file containing tests
# # @pytest.fixture(scope="module")
# # def app():
# #     # Create a new app instance for each test module
# #     application = create_app()
# #
# #     # Configure Flask app for testing with an in-memory SQLite database
# #     # Put Flask into testing mode
# #     # Use an in-memory SQLite database for tests
# #     # Event system is not needed
# #     # Set Flask into production mode by disabling debug mode (it affects error handling)
# #     application.config.update({
# #         'TESTING': True,
# #         'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
# #         'SQLALCHEMY_TRACK_MODIFICATIONS': False,
# #         'DEBUG': False
# #     })
# #
# #     # Create the database schema
# #     with application.app_context():
# #         Base.metadata.create_all(engine)
# #         yield application
# #         Base.metadata.drop_all(engine)
#
# # Set up a session for testing the databases
# @pytest.fixture(scope="function")
#
# # @pytest.fixture(scope="function")
# # def session(app):
# #     # Start a transaction for testing
# #     connection = engine.connect()
# #     transaction = connection.begin()
# #
# #     # Create a session using the connection
# #     local_session = sessionmaker(bind=connection, autocommit=False, autoflush=False)
# #     session = local_session()
# #
# #     try:
# #         yield session
# #     finally:
# #         # Close the session, rollback, and close the connection
# #         session.close()
# #         transaction.rollback()
# #         connection.close()
