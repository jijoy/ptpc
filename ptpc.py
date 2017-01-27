from collections import OrderedDict
import json
from config import *
from pytrackerv5 import PivotalIntegration
from tabulate import tabulate

def get_user_points():
    '''
    Gets user points for stories
    :return:
    '''
    owners = ['owner:'+owner for owner in USERS]
    query = ' OR '.join(owners)
    query = '('+query + ')'
    api = PivotalIntegration(API_KEY)
    response = api.get_project_memberships(TRACKER_PROJECT)
    id_name = {}
    # print response
    for item in response:
        id_name.__setitem__(item.get('person').get('id'),item.get('person').get('initials'))
    # print id_name
    state = ''
    if MANUAL_PLANNING:
        state = 'state:planned'
    else:
        state = 'state:unstarted'
    state = '('+state+')'
    query = '('+query+' AND '+state+')' if len(USERS) > 0 else state
    response = api.get_stories(TRACKER_PROJECT,filter=query)
    # response = api.get_stories(TRACKER_PROJECT)
    points_per_owner = {}
    if DEBUG:
        for item in response:
            print item.get('current_state')
        print 'Response %s'%json.dumps(response)
    for item in response:
        owner_ids = item.get('owner_ids')
        estimate = item.get('estimate',0)
        estimate_by_owner = estimate / len(owner_ids) if len(owner_ids) > 0 else 0
        for owner_id in owner_ids:
            points_per_owner.__setitem__(owner_id,points_per_owner.get(owner_id,0) + estimate_by_owner)
    user_points = {}
    for owner_id,points in points_per_owner.iteritems():
        if id_name.get(owner_id):
            user_points.__setitem__(id_name.get(owner_id),points)
    data = OrderedDict()
    if DEBUG:
        print user_points
    data.__setitem__("User",user_points.keys())
    data.__setitem__("Points",user_points.values())

    print tabulate(data,headers="keys")

if __name__ == '__main__':
    get_user_points()