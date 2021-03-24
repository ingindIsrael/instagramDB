import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    userID = Column(Integer, primary_key=True)
    userName = Column(String(250), unique=True, nullable=False) 
    fname = Column(String(250))
    lname = Column(String(250))
    email = Column(String(250), unique=True, nullable=False) 

class follower(Base):
    __tablename__ = 'follower'
    followID = Column(Integer, primary_key=True)
    userFromID = Column(Integer, ForeignKey('user.userID'))
    userToID = Column(Integer, ForeignKey('user.userID'))
    user = relationship(user)

class post(Base):
    __tablename__ = 'post'
    authorID = Column(Integer, ForeignKey('user.userID'))
    postID = Column(Integer, primary_key=True)
    user = relationship(user)
    
class comment(Base):
    __tablename__ = 'comment'
    commentID = Column(Integer, primary_key=True)
    authorID = Column(Integer, ForeignKey('user.userID'))
    postID = Column(Integer, ForeignKey('post.postID'))
    commentText = Column(String(250))
    user = relationship(user)
    post = relationship(post)

class media(Base):
    __tablename__ = 'media'
    mediaID = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('post.postID'))
    mediaType = Column(String(250), nullable=False)
    url = Column(String(250))
    post = relationship(post)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')