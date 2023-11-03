#!/usr/bin/env python
"""Models for Kasi Konnections."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)


class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    vehicle = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(100))

    
    def __init__(self, name, email, address, phone, vehicle, password):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.vehicle = vehicle
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

    def __repr__(self):
        return '<Driver{}>'.format(self.id)
    
    vehicle = db.relationship('Vehicle', back_populates='driver')
    DeliveryFromDriver = db.relationship('deliveryFromDriver', back_populates='driver')
    deliveryfromsupermarket = db.relatioship('deliverfromsupermarket', back_populates='driver')


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100))

    
    def __init__(self, name, email, address, phone, password):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
    
with app.app_context():
    db.create_all()
    db.session.add(Driver(name='<NAME>',email='<EMAIL>',address='<ADDRESS>',
                          phone='<PHONE>',password='<PASSWORD>'))
    db.session.add(Customer(name='<NAME>',email='<EMAIL>',address='<ADDRESS>',
                            phone='<PHONE>',password='<PASSWORD>'))
    db.session.commit()
    driver = Driver.query.filter_by(email='<EMAIL>').first()
    print(driver.check_password('<PASSWORD>'))
    print(Driver.query.all())
    print(Driver.query.filter_by(email='<EMAIL>').first())
    print(Driver.query.filter_by(email='<EMAIL>').first().check_password('<PASSWORD>'))
    customer = Customer.query.filter_by(email='<EMAIL>').first()
    print(customer.check_password('<PASSWORD>'))
    print(Customer.query.all())
    print(Customer.query.filter_by(email='<EMAIL>').first())
    print(Customer.query.filter_by(email='<EMAIL>').first()
          .check_password('<PASSWORD>'))
    

    def __repr__(self):
        return '<Customer %r>' % self.name
    
    orders = db.relationship('Order', back_populates='customer')
    
class Supermarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, address, phone, website, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website
        self.email = email
        
    def __repr__(self):
        return '<Supermarket %r>' % self.name
    
    products = db.relationship('Product', back_populates='supermarket')
    orders = db.relationship('Order', back_populates='supermarket')
    delivery = db.relationship('Delivery', back_populates='supermarket')
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'))

    def __init__(self, name, price, description, supermarket_id):
        self.name = name
        self.price = price
        self.description = description
        self.supermarket_id = supermarket_id

    def __repr__(self):
        return '<Product %r>' % self.name

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    order_time = db.Column(db.DateTime, nullable=False)
    order_status = db.Column(db.String(100), nullable=False)
    order_price = db.Column(db.Float, nullable=False)
    order_address = db.Column(db.String(200), nullable=False)
    order_phone = db.Column(db.String(15), nullable=False)
    order_items = db.Column(db.String(200), nullable=False)
    order_notes = db.Column(db.String(200), nullable=False)

    def __init__(self, customer_id, driver_id, order_time, order_status, order_price, order_address
                 , order_phone, order_items, order_notes):
        self.customer_id = customer_id
        self.driver_id = driver_id
        self.order_time = order_time
        self.order_status = order_status
        self.order_price = order_price
        self.order_address = order_address
        self.order_phone = order_phone
        self.order_items = order_items
        self.order_notes = order_notes

    def __repr__(self):
        return '<Order {}>'.format(self.id)
    
    customer = db.relationship('Customer', back_populates='orders')
    products = db.relationship('Product', back_populates='orders')
    supermarket = db.relationship('Order', back_populates='orders')
    
with app.app_context():
    db.create_all()
    db.session.add(Customer(name='Kasi',email='<EMAIL>',address='123 Main St',phone='1234567890',password='<PASSWORD>'))
    db.session.commit()
    user = Customer.query.filter_by(email='<EMAIL>').first()
    print(user.check_password('<PASSWORD>'))
    print(Customer.query.all())
    print(Customer.query.filter_by(email='<EMAIL>').first())
    print(Customer.query.filter_by(email='<EMAIL>').first().check_password('<PASSWORD>'))
    
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return '<OrderItem {}>'.format(self.id)
    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(100), nullable=False)
    vehicle_registration = db.Column(db.String(100), unique=True)
    vehicle_make = db.Column(db.String(100), nullable=False)
    vehicle_model = db.Column(db.String(100), nullable=False)
    vehicle_location = db.Column(db.String(100), nullable=False)
    vehicle_notes = db.Column(db.String(200), nullable=False)

    def __init__(self, name, vehicle_type, vehicle_registration, vehicle_make,
                  vehicle_model, vehicle_location, vehicle_notes):
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicle_registration = vehicle_registration
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_location = vehicle_location
        self.vehicle_notes = vehicle_notes

    def __repr__(self):
        return '<Vehicle {}>'.format(self.id)
    
    drivers = db.relationship('Driver', back_populates='vehicles')



class DeliveryFromSupermarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    driver_current_location = db.Column(db.String(200), nullable=False)
    delivery_location = db.Column(db.String(200), nullable=False)
    delivery_time = db.Column(db.String(6), nullable=False)
    delivery_status = db.Column(db.String(30), nullable=False)

    def __init__(self, driver_id, customer_id, supermarket_id, order_id, 
                 driver_current_location, delivery_location, delivery_time,
                delivery_status):
        self.driver_id = driver_id
        self.customer_id = customer_id
        self.order_id = order_id
        self.supermarket_id = supermarket_id
        self.driver_current_location = driver_current_location
        self.delivery_location = delivery_location
        self.delivery_time = delivery_time
        self.delivery_status = delivery_status

    def __repr__(self):
        return '<DeliveryFromSupermarket {}>'.format(self.id)
    
    driver = db.relationship('Driver', back_populates='deliveries_from_supermarkets')

class DeliveryFromDriver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    driver_current_location = db.Column(db.String(200), nullable=False)
    delivery_location = db.Column(db.String(200), nullable=False)
    delivery_time = db.Column(db.String(6), nullable=False)
    delivery_status = db.Column(db.String(30), nullable=False)

    def __init__(self, driver_id, customer_id, supermarket_id, order_id, 
                 driver_current_location, delivery_location, delivery_time,
                delivery_status):
        self.driver_id = driver_id
        self.customer_id = customer_id
        self.order_id = order_id
        self.supermarket_id = supermarket_id
        self.driver_current_location = driver_current_location
        self.delivery_location = delivery_location
        self.delivery_time = delivery_time
        self.delivery_status = delivery_status

    def __repr__(self):
        return '<DeliveryFromDriver {}>'.format(self.id)
    
    driver = db.relationship('Driver', back_populates='deliveries_from_drivers')


with app.app_context():
    db.create_all()
    db.session.add(Driver(name='<NAME>',email='<EMAIL>',address='<ADDRESS>',
                          phone='PHONE',password='<PASSWORD>'))
    db.session.commit()
    user = Driver.query.filter_by(email='<EMAIL>').first()
    print(user.check_password('<PASSWORD>'))
    print(Driver.query.all())
    print(Driver.query.filter_by(email='<EMAIL>').first())
    print(Driver.query.filter_by(email='<EMAIL>').first()
          .check_password('<PASSWORD>'))
    









"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()
    db.session.add(User(name='Kasi',email='<EMAIL>',password='<PASSWORD>'))
    db.session.commit()
"""

