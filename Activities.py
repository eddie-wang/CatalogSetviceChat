def createTagOption(client, input):
    key = input["key"]
    value = input["value"]
    response = client.create_tag_option( Key=key,Value=value)
    print response
    return response