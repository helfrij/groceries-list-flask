from flask_migrate import Migrate, upgrade


migrate = Migrate()


def run_migrations():
    upgrade()
