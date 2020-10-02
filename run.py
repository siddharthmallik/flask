from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('template.html', my_string="Siddharth!", my_list=[0,1,2,3,4,5])

@app.route("/about")
def about():
    return render_template(
        'template.html', my_string="helloSiddharth!", 
        my_list=[0,1,2,3,4,5], title="About")

@app.route("/contact")
def contact():
    return render_template(
        'template.html', my_string="HiSiddharth!", 
        my_list=[0,1,2,3,4,5], title="Contact Us")


if __name__ == '__main__':
    app.run(debug=True)