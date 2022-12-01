from urllib import response
import urllib.request as urllib, json

from configuration import API_ROOT_URL

class Client:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def data_reader(self, url):
        response = urllib.urlopen(url)
        data_json = json.loads(response.read())
        return data_json

    def contracts(self):
        url = API_ROOT_URL + '/contracts?apiKey=' + self.apiKey
        return self.data_reader(url)

    def contract(self, name):
        url = API_ROOT_URL + '/contracts='+ name +'apiKey=' + self.apiKey
        return self.data_reader(url)

    def stations(self):
        url = API_ROOT_URL + '/stations?apiKey=' + self.apiKey
        return self.data_reader(url)

    def contract_liststations(self, contract):
        url = API_ROOT_URL + '/stations?contract=' + contract +'&apiKey=' + self.apiKey
        return self.data_reader(url)

    def contract_station(self, contract, number):
        url = API_ROOT_URL + '/stations/'+ number+ '?contract=' + contract +'&apiKey=' + self.apiKey
        return self.data_reader(url)