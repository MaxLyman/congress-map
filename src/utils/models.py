from __future__ import annotations
from .extensions import db


class Member(db.Model):
    __tablename__ = "members"

    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name                = db.Column(db.Text, nullable=False)
    party               = db.Column(db.Text, nullable=False)
    created_at          = db.Column(db.DateTime, server_default=db.func.datetime("now"))
    bioguide_id         = db.Column(db.Text, unique=True)
    fec_candidate_id    = db.Column(db.Text)

    fec_ids = db.relationship(
        "MemberFecId",
        back_populates="member",
        cascade="all, delete-orphan",
    )

class Term(db.Model):
    member_id           = db.Column(db.Text, unique=True, primary_key=True)
    start_year          = db.Column(db.DateTime, nullable=False)
    end_year            = db.Column(db.DateTime, nullable=True)
    fec_candidate_id    = db.Column(db.Text)


class MemberFecId(db.Model):
    __tablename__ = "member_fec_ids"

    member_id = db.Column(
        db.Integer,
        db.ForeignKey("members.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    fec_candidate_id    = db.Column(db.Text, primary_key=True, nullable=False)
    election_year       = db.Column(db.Integer)

    member = db.relationship("Member", back_populates="fec_ids")


