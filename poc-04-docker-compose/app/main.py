import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "POC 04 - Docker Compose",
        "status": "running",
        "message": "Flask application is running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/db-health")
def db_health():
    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST", "db"),
            port=int(os.getenv("DB_PORT", "5432")),
            dbname=os.getenv("DB_NAME", "appdb"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.environ["DB_PASSWORD"],
            connect_timeout=3
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

        if result and result[0] == 1:
            return jsonify({
                "database": "postgresql",
                "status": "connected"
            }), 200

        return jsonify({"status": "database check failed"}), 503

    except (psycopg.Error, KeyError, ValueError) as error:
        app.logger.warning("Database health check failed: %s", error)
        return jsonify({"status": "database unavailable"}), 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "3000"))
    )
