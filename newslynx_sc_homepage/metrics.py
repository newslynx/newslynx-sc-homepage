from collections import defaultdict

from newslynx.sc import SousChef
from newslynx.lib import url
from newslynx.lib import dates
import pageone


class TimeOnHomepage(SousChef):

    def _gen_lookups(self):
        """
        Create a tree of url > content item ids.
        """
        # create containers
        self.url_lookup = defaultdict(list)

        # populate with ALL content items.
        for c in self.api.orgs.simple_content():
            u = c.pop('url', None)
            if u:
                self.url_lookup[url.prepare(u)].append(c['id'])

    def setup(self):
        """
        Generate url lookups.
        """
        self._gen_lookups()

    def run(self):
        """
        Fetch homepage URLs, lookup content item IDS, and set number of minutes
        it's been on the homepage.
        """
        p = self.options.pop('page')
        for link in pageone.get(p, **self.options):
            u = link.get('url')

            # smartly handle urls
            u = url.prepare(u, canonicalize=False)
            if u and not u in self.url_lookup:
                u = url.prepare(u, canonicalize=True)

            # yield metrics
            if u and u in self.url_lookup:
                cids = self.url_lookup[u]
                for cid in cids:
                    yield {
                        'datetime': dates.now(),
                        'content_item_id': cid,
                        'metrics': {
                            'time_on_homepage': self.recipe.get('minutes', 60)
                        }
                    }

    def load(self, data):
        """
        Create content timeseries.
        """
        d = list(data)
        status_resp = self.api.content.bulk_create_timeseries(data=d)
        return self.api.jobs.poll(**status_resp)
