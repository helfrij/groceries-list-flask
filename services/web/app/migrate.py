from flask_migrate import Migrate, upgrade


migrate = Migrate(directory='services/web/migrations')


def run_migrations():
    upgrade()
