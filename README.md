# Internet speed test flask app

This is a simple flask app that tests the internet speed of the network and stores the data in a database.

## Installation

1. Clone the repository
2. Install the requirements with `pip install -r requirements.txt`
3. Run `flask --app flaskr init-db` to initialize the database
4. Finally, run `flask run` to run the app

## Usage

- With a cron job do GET request to `/speedtest/run` to run a speed test that will be stored in the database every X
  minutes/hours/days
- Do a GET request to `/speedtest/today` to get the speed tests of the last 24 hours

## Evolution

- [ ] Weekly view
- [ ] Monthly view
- [ ] Yearly view
- [ ] Custom view
- [ ] Send alert on telegram when the speed is below a certain level