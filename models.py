from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)
    tele_handle = Column(String(20), nullable=False, unique=True)
    name = Column(String(100))
    dragon_id = Column(Integer, ForeignKey('users.id'), index=True)
    # ref: https://github.com/sqlalchemy/sqlalchemy/issues/1403#issue-384617192
    registered = Column(Boolean, nullable=False, default=False, server_default="0")
    dragon = relationship('User', remote_side=[id], backref=backref('trainer', uselist=False), uselist=False, post_update=True)

class UserDetails(Base):
    __tablename__ = 'user_details'

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)
    likes = Column(Text)
    dislikes = Column(Text)

class MessageMapping(Base):
    __tablename__ = 'message_mapping'

    sender_message_id = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    receiver_message_id = Column(Integer, nullable=False)
    receiver_chat_id = Column(Integer, nullable=False)
    deleted = Column(Boolean, nullable=False, default=False, server_default="0")
