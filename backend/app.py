from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health", methods = ["GET"])
def health():

    return jsonify({
        "mensaje": "TrendMarket funcionando",
        "estado": "correcto"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)