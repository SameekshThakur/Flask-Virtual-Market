from market import db, bcrypt
from market import login_manager
from flask_login import UserMixin

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

class Item(db.Model) :
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024))
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self) :
        return f"Item {self.name}"
    
    def buy(self, user) :
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()


    def sell(self, user) :
        self.owner = None
        user.budget += self.price
        db.session.commit()
    
    

class User(db.Model, UserMixin) :
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=40), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable = False, unique = True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), default = 1000, nullable = False)
    # Here backreference helps us to find the items owned by the user and lazy is important for db to understand
    items = db.relationship('Item', backref="owned_user", lazy=True)

    @property
    def password(self) :
        return self.password
    
    @password.setter
    def password(self, plain_password) :
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password_correction(self, attempted_password) :
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    @property
    def prettier_budget(self) :
        if len(str(self.budget)) >=4 :
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else :
            return f"{self.budget}$"
        
    def can_purchase(self, item_obj) :
        return self.budget >= item_obj.price
    
    def can_sell(self, item_obj) :
        return item_obj in self.items  # this self.items refer to the items present in Item which defines relationship that wheather the item is under owner or not
    


