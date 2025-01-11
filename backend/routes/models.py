from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class CompanyLogin(db.Model):
    __tablename__ ="companylogin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    FK_companyId = db.Column(db.Integer, db.ForeignKey('companyaccount.companyId', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    company = db.relationship('CompanyAccount', foreign_keys=[FK_companyId], backref='CompanyLogin')

    def __repr__(self):
        return f"<CompanyLogin(companyId={self.companyId}, username={self.username})>"

class CompanyAccount(db.Model):
    __tablename__ = 'companyaccount'

    companyId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(256), unique=True, nullable=False)
    activeAccount = db.Column(db.Boolean, nullable=False)
    carbonBalance = db.Column(db.Integer, nullable=False)
    cashBalance = db.Column(db.Float, nullable=False)
    createdDatetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedDatetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<CompanyAccount(companyId={self.companyId}, companyName='{self.companyName}')>"

class OutstandingRequest(db.Model):
    __tablename__ = 'outstandingrequest'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyId = db.Column(db.Integer, db.ForeignKey('companyaccount.companyId', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    requestorCompanyId = db.Column(db.Integer, db.ForeignKey('companyaccount.companyId', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    carbonUnitPrice = db.Column(db.Float, default=0, nullable=False)
    carbonQuantity = db.Column(db.Float, default=0, nullable=False)
    requestReason = db.Column(db.Text, nullable=True)
    requestStatus = db.Column(db.String(50), nullable=False)
    requestType = db.Column(db.String(50), nullable=False)
    createdDatetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedDatetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    company = db.relationship('CompanyAccount', foreign_keys=[companyId], backref='OutstandingRequest')
    requestorCompany = db.relationship('CompanyAccount', foreign_keys=[requestorCompanyId], backref='RequestReceived')

    def __repr__(self):
        return f"<OutstandingRequest(id={self.id}, companyId={self.companyId}, requestorCompanyId={self.requestorCompanyId})>"

class RequestReceived(db.Model):
    __tablename__ = 'requestreceived'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requestId = db.Column(db.Integer, db.ForeignKey('outstandingrequest.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    alertDatetime = db.Column(db.DateTime, nullable=False)
    alertText = db.Column(db.Text, nullable=False)
    alertStatus = db.Column(db.String(50), nullable=False)
    alertViewDate = db.Column(db.DateTime, nullable=True)
    createdDatetime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedDatetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    request = db.relationship('OutstandingRequest', backref='RequestReceived')

    def __repr__(self):
        return f"<RequestReceived(id={self.id}, requestId={self.requestId})>"
