import urllib2
import json


class MojangAPI:

    def _get_json(self, url):
        req = urllib2.Request(
            url=url, headers={'Content-Type': 'application/json'})
        response = json.loads(urllib2.urlopen(req).read())

        return response

    def _post_json(self, url, data):
        req = urllib2.Request(
            url=url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        response = json.loads(urllib2.urlopen(req).read())

        return response

    def service_statuses(self, service=None):
        url = 'http://status.mojang.com/check'

        if service is not None:
            url = url + '?service=' + service

        statuses = self._get_json(url)

    def mojang_news(self):
        url = 'http://status.mojang.com/news'

        return self._get_json(url)

    def get_uuid(self, username):
        url = 'https://api.mojang.com/profiles/page/1'

        data = {
            'name': username,
            'agent': 'minecraft'
        }

        uuid = self._post_json(url, data)

        if uuid['size'] is not 1:
            return None

        return uuid['profiles'][0]
