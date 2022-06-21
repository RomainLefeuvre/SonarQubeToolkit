import configparser
from typing import List
import requests

from dto.component_measure import ComponentMeasureDTO




class SonarQubeRestClient:
    def __init__(self, config_uri):
        config = configparser.ConfigParser()
        config.read(config_uri)

        self.host = config['sonarQube']['host']
        self.port = config['sonarQube']['port']
        self.token = config['sonarQube']['token']
        self.url = f'http://{self.host}:{self.port}/'

    def get_metric_keys(self) -> List[str]:
        raw_response = self._get_request('api/metrics/search', {'ps': 200})
        return [metric['key'] for metric in raw_response['metrics']]

    def get_components_keys(self) -> List[str]:
        params = {'ps': 200, 'qualifiers': 'TRK', 'p': 1}
        raw_response = self._get_request('api/components/search', params)
        return [component['key'] for component in raw_response['components']]

    def get_component_measures(self, metrics_keys, component_key) -> ComponentMeasureDTO:
        params = {'metricKeys': ','.join(metrics_keys), 'component': component_key}
        raw_response = self._get_request('api/measures/component', params)
        return raw_response

    def create_project(self, name, project_key):
        req = self._post_request('api/projects/create', {'project': project_key, 'name': name})
        return req

    # Todo Handle multiple pages responses
    def _get_request(self, endpoint, params):
        try:
            req = requests.get(self.url + endpoint, auth=(self.token, ""), params=params)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return "An Http Error occurred:" + repr(err)
        except requests.exceptions.ConnectionError as err:
            return "An Error Connecting to the API occurred:" + repr(err)
        except requests.exceptions.Timeout as err:
            return "A Timeout Error occurred:" + repr(err)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)
        return req.json()

    def _post_request(self, endpoint, data):
        try:
            req = requests.post(self.url + endpoint, auth=(self.token, ""), data=data)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return "An Http Error occurred: " + repr(err)
        except requests.exceptions.ConnectionError as err:
            return "An Error Connecting to the API occurred: " + repr(err)
        except requests.exceptions.Timeout as err:
            return "A Timeout Error occurred: " + repr(err)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred"  + repr(err)
        return req.json()


if __name__ == '__main__':
    sonarClient = SonarQubeRestClient('config.ini')
    keys = sonarClient.get_metric_keys()
    components = sonarClient.get_components_keys()
    print(sonarClient.get_component_measures(keys, components[0]))
    print(sonarClient.create_project('t', 't'))
