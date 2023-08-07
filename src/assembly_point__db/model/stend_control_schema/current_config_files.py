from db_utils import CustomQuery
from db_utils.modules.db import db
from sqlalchemy_serializer import SerializerMixin
from src.assembly_point__db.model.stend_control_schema.stend_list import StendList


class CurrentConfigFiles(db.Model, SerializerMixin):
    __tablename__ = 'current_config_files'
    __table_args__ = {'schema': 'stend_control_schema'}

    stend = db.Column(db.Integer, db.ForeignKey("stend_control_schema.stend_list.stend_id"))
    stend_model = db.relationship(
        StendList,
        foreign_keys=[stend],
        query_class=CustomQuery,
        uselist=False,
        lazy='joined'
    )
    name = db.Column(db.String(128))
    md5 = db.Column(db.String(32))
    crc32 = db.Column(db.Integer)
    data = db.Column(db.LargeBinary)
    time = db.Column(db.DateTime)
    version = db.Column(db.String(45))
