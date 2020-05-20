from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("index.html")


@app.route("/Futbol")
def url_Futbol():
 	Equipos = [
 		"Pumas",
 		"Barcelona"
 	]
 	return render_template("Futbol.html", Equipos=Equipos, nombre="Equipos")

if __name__ == "__main__":
	app.run(debug=True)