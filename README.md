# JCDecauxBack

Backend of a JCDecaux Dashboard based on JCDecaux online API.

Using Flask Framework.

# Launch project

Get your api token from https://developer.jcdecaux.com

```bash
pip install -r requirement.txt
export FLASK_APP=apiJCD/api.py
flask run
```

| Endpoint                                                                      | Returns                              |
| ----------------------------------------------------------------------------- | ------------------------------------ |
| `/contracts`                                                                   | List of contracts                    |
| `/stations`                             | List of stations                        |
| `/contracts/<contract>/stations`                                              | List of stations for given contract |
| `/contracts/<contract>/stations/<station_number>`                                  | Station detail                     |




