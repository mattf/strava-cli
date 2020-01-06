from ._helpers import client, url, json


def post_uploads(filename, data_type):
    response = client.post(url(f'/uploads'),
                           files={'file': open(filename, 'rb')},
                           data={'data_type': 'fit'})
    return json(response)


def get_uploads(upload_id):
    response = client.get(url(f'/uploads/{upload_id}'))
    return json(response)
