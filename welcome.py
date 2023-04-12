from flask import Flask,render_template

data=[{"firstname":"Akriti " , "lastname ":"Mishra" ,"company":"Abzooba"},
       {"firstname":"Sunny " , "lastname ":"Singh" ,"company":"Cognizant"},
       {"firstname":"Priya " , "lastname ":"Mehra" ,"company":"Tcs"},
      ]
app=Flask(__name__)

@app.route("/")
def home():
   return render_template('home.html')

if __name__ =='__main__':
   app.run(debug=True)
   print('oroo')
