from __future__ import annotations

import os
from dataclasses import dataclass, asdict

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.endpoints.census_gov_api.census_service import CensusService
from src.endpoints.congress_gov_api.congress_service import CongressService


@dataclass
class Services:
    census_service: CensusService
    congress_service: CongressService


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/congress_map.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    from src.utils.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)    

    app.extensions["services"] = Services(
        census_service=CensusService(),
        congress_service=CongressService()
    )

    # Register models so SQLAlchemy metadata & migrations can see them.
    import src.utils.models
   
    return app


class DBUtils:
    def set_db(self, db: SQLAlchemy):
        self.db = db
