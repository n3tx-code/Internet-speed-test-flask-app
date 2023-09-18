import datetime
import sqlite3


def generate_data_for_previous_day():
    # get last two last speedtest records
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM speedtest ORDER BY date DESC LIMIT 2")
    results = cursor.fetchall()

    if len(results) < 2:
        # no previous record
        return

    last_speedtest_date = datetime.datetime.strptime(results[0][4], '%Y-%m-%d %H:%M:%S')
    previous_speedtest_date = datetime.datetime.strptime(results[1][4], '%Y-%m-%d %H:%M:%S')
    if last_speedtest_date.date() == previous_speedtest_date.date():
        # do nothing if they are on the same day
        return

    # if not, then generate data for the previous day
    previous_speedtest_date_start = previous_speedtest_date.replace(hour=0, minute=0, second=0)
    previous_speedtest_date_end = previous_speedtest_date.replace(hour=23, minute=59, second=59)

    # get data for the previous day
    cursor.execute(
        "SELECT AVG(ping) as avg_ping, MIN(ping) as min_ping, MAX(ping) as max_ping, "
        "AVG(download) as avg_download, MIN(download) as min_download, MAX(download) as max_download, "
        "AVG(upload) as avg_upload, MIN(upload) as min_upload, MAX(upload) as max_upload "
        "FROM speedtest WHERE date BETWEEN '" + previous_speedtest_date_start.strftime(
            '%Y-%m-%d %H:%M:%S') + "' AND '" + previous_speedtest_date_end.strftime('%Y-%m-%d %H:%M:%S') + "'")
    result = cursor.fetchone()

    # create day_speedtest record
    cursor.execute(
        "INSERT INTO day_speedtest(ping_max, ping_min, ping_avg, download_max, download_min, download_avg, upload_max, upload_min, upload_avg, date) VALUES ('" + str(
            result[0]) + "', '" + str(result[1]) + "', '" + str(result[2]) + "', '" + str(result[3]) + "', '" + str(
            result[4]) + "', '" + str(result[5]) + "', '" + str(result[6]) + "', '" + str(result[7]) + "', '" + str(
            result[8]) + "', '" + previous_speedtest_date_start.strftime("%Y-%m-%d") + "')")
    conn.commit()

    # delete previous day speedtest
    cursor.execute("DELETE FROM speedtest WHERE date BETWEEN '" + previous_speedtest_date_start.strftime(
        '%Y-%m-%d %H:%M:%S') + "' AND '" + previous_speedtest_date_end.strftime('%Y-%m-%d %H:%M:%S') + "'")
    conn.commit()
    conn.close()
