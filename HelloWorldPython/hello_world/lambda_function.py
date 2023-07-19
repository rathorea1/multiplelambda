import os
import re

def lambda_handler(event, context):
    if event['triggerSource'] != 'TokenGeneration_HostedAuth' and event['triggerSource'] != 'TokenGeneration_RefreshTokens':
        return event;
    request = event['request']
    userAttributes = request['userAttributes'] 
    if userAttributes['cognito:user_status'] != 'EXTERNAL_PROVIDER':
        return event;
    cGroups = userAttributes.get('custom:groups')
    groupsToOverride = ['AllClients']
    if cGroups != None:
        groups = re.findall(r'\w+', cGroups)
        for aGroup in groups:
            group = os.environ.get(aGroup);
            if group != None:
                groupsToOverride.append(group)
    event['response'] = {
        "claimsOverrideDetails": {
            "groupOverrideDetails": {
                "groupsToOverride": groupsToOverride
            }
        }
    }
    return event