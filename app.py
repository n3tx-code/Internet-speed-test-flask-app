import json
import sqlite3
import subprocess

from flask import Flask, Response, render_template

from tools import generate_data_for_previous_day

app = Flask(__name__)


@app.route('/speedtest/run')
def run_speedtest():
    test_result = subprocess.run(['speedtest', '--f', 'json-pretty'], stdout=subprocess.PIPE).stdout
    json_test_result = json.loads(test_result)
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO speedtest (ping, download, upload) VALUES ('" +
                   str(json_test_result['ping']['latency']) + "', '" +
                   str(json_test_result['download']['bandwidth'] / 125000) + "', '" +
                   str(json_test_result['upload']['bandwidth'] / 125000) + "')")
    conn.commit()
    conn.close()
    generate_data_for_previous_day()
    return Response(status=200)


@app.route('/speedtest/today')
def speedtest_today():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT ping, download, upload, datetime(date, 'localtime') FROM speedtest WHERE date >= date('now', '-1 day')")
    results = cursor.fetchall()
    downloads = []
    uploads = []
    pings = []
    labels = []
    for row in results:
        pings.append(row[0])
        downloads.append(row[1])
        uploads.append(row[2])
        labels.append(row[3])
    # return render_template('speedtest/day.html', results=results)
    return render_template('speedtest/day.html', downloads=downloads, uploads=uploads, pings=pings, labels=labels)


if __name__ == '__main__':
    app.run()
