
from flask import Flask , render_template ,flash, request, redirect, url_for
import test


app = Flask(__name__)
app.secret_key = '2f0b6bfabfd2e24c1b5c98d4'

def swap(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form" , methods=["GET", "POST"])
def form():
    if request.method == "POST":

        req = request.form
        print (req)
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for:   {',   '.join(missing)}"
            return render_template("index.html", feedback=feedback)
        
        else:
            
            x = list()

            for k, v in req.items():
                try:    
                    x.append(float(v))
                except ValueError:
                    feedback = f"The value of '{k}' must be a number"
                    return render_template("form.html", feedback=feedback)
            

            print(x)
            result = test.predict([x])
            if result :
                flash('The prediction is you have diabetes', 'danger')
            else:
                flash('The prediction is you DONT have diabetes', 'success')
            
            return redirect(request.url)
            

        return redirect(request.url)
    return render_template('form.html')


