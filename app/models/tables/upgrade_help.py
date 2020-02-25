from sqlalchemy import Column, String
from ...extensions import db
from ..mixins import BaseMixin


class UpgradeHelp(db.Model, BaseMixin):
    __tablename__ = "upgrade_help"
    __bind_key__ = "static_data"

    description = Column(String)

    def to_dict(self, minimal: bool = False) -> dict:
        minimal_dict = BaseMixin.to_dict(self, minimal)

        if minimal:
            return minimal_dict

        return {
            **minimal_dict,
            "description": self.description
        }
