from collections import defaultdict
import re


class NagiosStatus(object):

    RE_BLOCKSTART = re.compile('(\w+)\s*{')
    RE_BLOCKEND = re.compile('^\s*}\s*$')
    RE_DEF = re.compile('(\S+)\s*=(.+)$')

    def __init__(self, f):
        self.f = f
        self.hosts = defaultdict(list)
        self.services = defaultdict(list)
        try:
            self._parse_blocks()
        except StopIteration:
            pass

    def _parse_blocks(self):
        while True:
            l = self.f.next()
            m = self.RE_BLOCKSTART.search(l)
            if m:
                defs = self._parse_defs()
                if m.group(1) == 'servicestatus':
                    self.services[defs['host_name']].append(defs)
                elif m.group(1) == 'hoststatus':
                    self.hosts[defs['host_name']].append(defs)

    def _parse_defs(self):
        defs = {}
        while True:
            l = self.f.next()
            m = self.RE_BLOCKEND.search(l)
            if m:
                return defs

            m = self.RE_DEF.search(l)
            if m:
                defs[m.group(1)] = m.group(2)
