from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Community(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    schedule = Column(String)
    picture = Column(String)
    comments = relationship("Comment",backref="communities")
    contact = Column(String)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    community_id = Column(Integer, ForeignKey('communities.id'))
    creator = Column(String)
    replies = relationship('Reply', backref='comments')


class Reply(Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    comment_id = Column(Integer, ForeignKey('comments.id'))

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(EmailType)

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, index=True)
    community_id = Column(Integer, ForeignKey('communities.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    value = Column(Integer)



