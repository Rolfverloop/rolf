bruin=set(['best', 'beukellaan', 'helmond', 'helmond brouwhuis', 'deurne'])
groen=set(['best', 'beukellaan', 'geldrop', 'heeze', 'weert'])


print('De volgende stationnen komen overeen: {}'.format(bruin.intersection(groen)))
print('De volgende stationnen komen overeen: {}'.format(bruin.union(groen)))
