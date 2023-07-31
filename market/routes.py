from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterationForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page() :
    return render_template("home.html", user_name = "Sameeksh")


@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page() :
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if purchase_form.validate_on_submit() :
        if request.method == "POST" :
            purchased_item = request.form.get('purchased_item')
            p_item_obj = Item.query.filter_by(name=purchased_item).first()
            if p_item_obj :
                if current_user.can_purchase(p_item_obj) :
                    p_item_obj.buy(current_user)
                    flash(f"Congratulations! You purchased {p_item_obj.name} for {p_item_obj.price}$", category="success")
                else:
                    flash(f"Unfortunately, you don't have enough money to purchase {p_item_obj.name} !", category="danger")

            sold_item = request.form.get('sold_item')
            s_item_obj = Item.query.filter_by(name=sold_item).first()
            if s_item_obj :
                if current_user.can_sell(s_item_obj) :
                    s_item_obj.sell(current_user)
                    flash(f"Congratulations! You sold {s_item_obj.name} to the market!", category="success")
                else:
                    flash(f"Something went wrong with selling {s_item_obj.name} !", category="danger")



            return redirect(url_for('market_page'))
        
    if request.method == "GET" :
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template("main_market.html", item_names = items, purchase_form=purchase_form, owned_items=owned_items, sell_form=sell_form)

@app.route("/register", methods = ["GET", "POST"]) 
def register_page() :
    form = RegisterationForm()
    if form.validate_on_submit() :
        user_to_create = User(user_name=form.username.data, email_address=form.emailAddress.data, password=form.password_1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully ! You are now logged in as : {user_to_create.user_name} ", category="success")
        return redirect(url_for('market_page'))
    
    if form.errors != {} : # This is a dictionary which holds all the errors caught during registration and we want users to display that result
        for err_message in form.errors.values() :
            flash(f"There was an error with creating a user account : {err_message}", category='danger')

    return render_template("register.html", register_form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page() :
    form = LoginForm()
    if form.validate_on_submit() :
        user_login = User.query.filter_by(user_name=form.username.data).first()
        if user_login and user_login.check_password_correction(attempted_password=form.password.data) :
            login_user(user_login)
            flash(f"Successfully Logged In as : {user_login.user_name}", category="success")
            return redirect(url_for('market_page'))
        
        else :
            flash(f"Username and Password does not match ! Please try again ", category="danger")
    return render_template('login.html', login_form = form)


@app.route("/logout")
def logout_page() :
    logout_user()
    flash(f"You have been logged out!", category="info")
    return redirect(url_for('home_page'))