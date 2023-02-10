import json
import requests
from secrets import clientId, clientSecret
import base64

def get_access_token():
    redirect_uri = 'http://localhost:3000/callback'
    state = "3883839392921Gf0"
    scope = "user-read-private user-read-email playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read"


    auth_url = f'https://accounts.spotify.com/authorize?response_type=code&client_id={clientId}&redirect_uri={redirect_uri}&state={state}&scope={scope}'

    loc_url ="http://localhost:3000/callback?code=AQC30Qg914nc4OsWDIcneVMUQNO0VgavZ7hyDkAR4xebDJtMhX9Ng-54WuxLJi-nGi45JGVMUFGL7PhaoASFGwTlBJ_pgcFVQj1KFn7saye2jXSQkiO3zrlhXuVPR5XUel02YpQC9AZ9YN_VBw5jlJdWc1sg4nFEh0mGI3mAMpQWNQ0lqbJHX7HTWKnpbTRaY03F88kxhqBDRgCPC9PrnYUtaDR_25qIVTFYCHanYt4bm8v9CWL7GFdRMENsbDCbgxJfEYW9qtNt6AR9vheBYcti356eR4OWT9de8tZGR22HgRL_n2KdsN7wjh203rCyG-ClZU-3yzAiLZ9P3RoBRTK46idDUg4s_RXB9AIRqFh3LjKoBWSoc7PMc4Mp25ok4nronwRx-MPDb8ByeyK8hMSgjg&state=3883839392921Gf0"
    code = "AQC30Qg914nc4OsWDIcneVMUQNO0VgavZ7hyDkAR4xebDJtMhX9Ng-54WuxLJi-nGi45JGVMUFGL7PhaoASFGwTlBJ_pgcFVQj1KFn7saye2jXSQkiO3zrlhXuVPR5XUel02YpQC9AZ9YN_VBw5jlJdWc1sg4nFEh0mGI3mAMpQWNQ0lqbJHX7HTWKnpbTRaY03F88kxhqBDRgCPC9PrnYUtaDR_25qIVTFYCHanYt4bm8v9CWL7GFdRMENsbDCbgxJfEYW9qtNt6AR9vheBYcti356eR4OWT9de8tZGR22HgRL_n2KdsN7wjh203rCyG-ClZU-3yzAiLZ9P3RoBRTK46idDUg4s_RXB9AIRqFh3LjKoBWSoc7PMc4Mp25ok4nronwRx-MPDb8ByeyK8hMSgjg"
    # auth_resp = requests.get(url=auth_url)
    # print(auth_resp.url)


    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    refresh_token="AQAuhq2nHlWQIpSIXJP4R1Tr3XkjwujvoTXox6PeCTBA-RkI1_miu16YT_3lH64KAyYj-d5TESB4rYDC8RPkpaai4KmIDkb-k2VuA8rWLDBpuGNMdyeyj1pqS2SV4UZfXDk"

    headers['Authorization'] = f"Basic {base64Message}"
    # data['grant_type'] = "authorization_code"
    data['grant_type'] = "refresh_token"
    # data['grant_type'] = "authorization_code"
    # data['code'] = code
    data['refresh_token'] = refresh_token
    # data['redirect_uri'] = redirect_uri

    r = requests.post(url, headers=headers, data=data)
    print(json.dumps(r.json(), indent=2))

    access_token= r.json()['access_token']
    return access_token



