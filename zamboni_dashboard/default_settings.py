class DefaultSettings(object):
    DASHBOARD_NAME = 'Zamboni Dashboard'
    OPS_BUG_URL = 'https://bit.ly/amo_ops_bug'
    OPS_DOCS_URL = 'https://mana.mozilla.org/wiki/display/websites/addons.mozilla.org'
    ENABLED_MODULES = ['ganglia', 'graphite', 'nagios', 'pingdom']
    
    # GANGLIA_BASE = 'https://ganglia.mozilla.org/phx1'  # deprecated
    GANGLIA_DEFAULT_REPORTS = ['load_report', 'cpu_report',
                       'mem_report', 'network_report']
    GANGLIA_GROUPS = [('Web', 'https://ganglia.mozilla.org/phx1', 'addons', ['apache_report',
                                     'apache_server_report',
                                     'nginx_active_connections',
                                     'nginx_response_report',
                                     'nginx_server_report']),
                    ('Memcache', 'https://ganglia.mozilla.org/phx1', 'Memcache AMO Cluster', ['memcached_report']),
                    ('Redis', 'https://ganglia.mozilla.org/phx1', 'amo-redis', ['amo_redis_prod_report'])
                    ]
    GRAPHITE_BASE = 'https://graphite-phx.mozilla.org'
    GRAPHITE_SITE_URLS = {
						'addons': 'https://addons.mozilla.org',
						'dev': 'https://addons-dev.allizom.org',
						'stage': 'https://addons.allizom.org',
						'marketplace': 'https://marketplace.mozilla.org',
						'marketplace-dev': 'https://marketplace-dev.allizom.org',
						'marketplace-stage': 'https://marketplace.allizom.org',
						}
    GRAPHITE_SITES = {
					'addons': 'addons',
					'dev': 'addons-dev',
					'stage': 'addons-stage',
					'marketplace': 'addons-marketplace',
					'marketplace-dev': 'addons-marketplacedev',
					'marketplace-stage': 'addons-marketplacestage',
					}
    GRAPHITE_DEFAULT_SITE = 'addons'
    GRAPHITE_SITE_NAMES = {
					'addons': 'Addons',
					'dev': 'Addons Dev',
					'stage': 'Addons Stage',
					'marketplace': 'Marketplace',
					'marketplace-dev': 'Marketplace Dev',
					'marketplace-stage': 'Marketplace Stage',
					}
    NAGIOS_STATUS_FILE = ''
    NAGIOS_STATUS_URL = ''
    NAGIOS_SERVICE_GROUPS = [('Web',
                       ['web%d.addons.phx1.mozilla.com' % i
                        for i in range(1, 31)],
                       ['zamboni monitor:8080', 'marketplace monitor:8081']),
                      ('Elasticsearch',
                       ['elasticsearch%d.webapp.phx1.mozilla.com' % i
                        for i in range(1, 4)],
                       ['color - Elasticsearch',
                        'procs - Elasticsearch']),
                      ('Redis',
                       ['redis%d.addons.phx1.mozilla.com' % i
                        for i in range(1, 3)],
                       ['amo-redis - tcp:6379',
                        'amo-redis - tcp:6381']),
                      ('Virtual Server: addons.mozilla.org',
                       ['addons.zlb.phx.mozilla.net'],
                       ['http - addons.mozilla.org',
                        'https - addons.mozilla.org',
                        'addons.mozilla.org - string blocklist',
                        'addons.mozilla.org - string Recommended',
                        'addons.mozilla.org - string Themes1',
                        'addons.mozilla.org - string Add-ons']),
                      ('Virtual Server: marketplace.mozilla.org',
                       ['marketplace.zlb.phx.mozilla.net'],
                       ['http - marketplace.m.o',
                        'https - marketplace.m.o']),
                      ('Virtual Server: versioncheck.addons.mozilla.org',
                       ['addons-versioncheck-single1.zlb.phx.mozilla.net',
                        'addons-versioncheck-single2.zlb.phx.mozilla.net',
                        'addons-versioncheck-single3.zlb.phx.mozilla.net'],
                       ['vamo-www',
                        'vamo zamboni monitor']),
                      ('Virtual Server: versioncheck-bg.addons.mozilla.org',
                       ['addons-versioncheck-single1.zlb.phx.mozilla.net',
                        'addons-versioncheck-single2.zlb.phx.mozilla.net',
                        'addons-versioncheck-single3.zlb.phx.mozilla.net'],
                       ['vamo-bg-www']),
                     ]
    PINGDOM_USER = ''
    PINGDOM_PASS = ''
    PINGDOM_KEY = ''

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 180
