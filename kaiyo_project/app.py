from flask import Flask, escape, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "super secret key"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False


#List to store all of user's furniture 
purchased_furniture = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        checkbox_list = []
        furniture_dict = {}
        print(request.form.getlist('mycheckbox'))
        checkbox_list = request.form.getlist('mycheckbox')
        #Use getlist to account for multiple selections
        if not checkbox_list:
            #If no checkboxes selected flash error
            print("ERROR!")
            flash("Please select at least 1 furniture to purchase!")
            return redirect(url_for('index'))
        else:
            #Store selected checkboxes
            furniture_dict['furnitures'] = checkbox_list
            purchased_furniture.append(furniture_dict)

    return render_template('index.html', purchased_furniture=purchased_furniture)



if __name__ == '__main__':
    app.run(debug=True)