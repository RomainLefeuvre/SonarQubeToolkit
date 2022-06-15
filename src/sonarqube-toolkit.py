import configparser
from typing import List
import requests

from dto.component_measure import ComponentMeasureDTO

config = configparser.ConfigParser()
config.read('config.ini')

host = config['sonarQube']['host']
port = config['sonarQube']['port']
token = config['sonarQube']['token']


class SonarQubeRestClient:
    def __init__(self):
        self.url = f'http://{host}:{port}/'

    def get_metric_keys(self) -> List[str]:
        raw_response = self._request('api/metrics/search', {'ps': 200})
        return [metric['key'] for metric in raw_response['metrics']]

    def get_components_keys(self) -> List[str]:
        params = {'ps': 200, 'qualifiers': 'TRK', 'p': 2}
        raw_response = self._request('api/components/search', params)
        return [component['key'] for component in raw_response['components']]

    def get_component_measures(self, metrics_keys, component_key) -> ComponentMeasureDTO:
        params = {'metricKeys': ','.join(metrics_keys), 'component': component_key}
        raw_response = self._request('api/measures/component', params)
        return raw_response

    # Todo Handle multiple pages responses
    def _request(self, endpoint, params):
        req = requests.get(self.url + endpoint, auth=(token, ""), params=params)
        return req.json()


if __name__ == '__main__':
    sonarClient = SonarQubeRestClient()
    keys = sonarClient.get_metric_keys()
    components = sonarClient.get_components_keys()
    print(sonarClient.get_component_measures(keys, 'test'))
