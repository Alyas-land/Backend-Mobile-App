from flask import render_template

class VisitorController:

    def index(self):
        return render_template('index.html')