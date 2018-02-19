from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def allRestaurants():
    return "All restaurant menus"

@app.route('/restaurants/new')
def newRestaurant():
    return "New restaurant menu"

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "You are editing restaurant " + str(restaurant_id) + "."

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "You are deleting restaurant " + str(restaurant_id) + "."

@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu')
def viewMenu(restaurant_id):
    return "You are viewing the menu for restaurant " + str(restaurant_id) + "."

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "You are adding a menu item to restaurant " + str(restaurant_id) + "."

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "You are editing menu item " + str(menu_id) + " from restaurant " + str(restaurant_id) + "."

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "You are about to delete menu item " + str(menu_id) + " from restaurant " + str(restaurant_id) + "."

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
