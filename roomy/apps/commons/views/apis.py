
def recaptcha_verify(response):
    from urllib.parse import urlencode
    from urllib.request import urlopen
    import json
    import requests

    response = requests.get(
        'https://www.google.com/recaptcha/api/siteverify',
        params={
            'secret': "6LfrJ90UAAAAABSYrNdEy-4Athxw3i3jeMT3OoTd",
            'response': response,
            # 'remote_ip': remote_ip,
        },
        # headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    )

    json_response = response.json()
    return json_response
    # URIReCaptcha = ''
    # recaptchaResponse = body.get('recaptchaResponse', None)
    # private_recaptcha = response
    # remote_ip = request.remote_addr
    # params = urlencode()
    #
    # # print params
    # data = urlopen(URIReCaptcha, params.encode('utf-8')).read()
    # result = json.loads(data)
    # success = result.get('success', None)
    #
    # if success == True:
    #     print('reCaptcha passed')
    # else:
    #     print('recaptcha failed')
