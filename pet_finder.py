from secrets import API_KEY, TOKEN
import requests


def find_random_pet():
    resp = requests.get('https://api.petfinder.com/v2/animals', params = {'limit':'1'}, headers={'Authorization': 'Bearer  eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjUwYzAwNTgxMGI3NmJiYmVmN2JhNDk1ODliNjU4MjNkMzhlNDE4YTBmMzUyODg0OGM1OTMyMGJjMDgyNThlMGE3ODM0YjkyNjc0N2UzNzVjIn0.eyJhdWQiOiJGTVlNbHY0SHZNMVJzYUdRSHg4b1poZEFNaFJGenRlcWJvdWRtdDMzaEZ1VElhZ3VubiIsImp0aSI6IjUwYzAwNTgxMGI3NmJiYmVmN2JhNDk1ODliNjU4MjNkMzhlNDE4YTBmMzUyODg0OGM1OTMyMGJjMDgyNThlMGE3ODM0YjkyNjc0N2UzNzVjIiwiaWF0IjoxNTU1NzE0NDg2LCJuYmYiOjE1NTU3MTQ0ODYsImV4cCI6MTU1NTcxODA4Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.zDtRNYTvNFtkxiPQ03Q6EAuQRg_1LmFyQeLWb_IAIGzkFzL6zp1-ssvFSjRmoFV1Fjc5P1rgZfIKGsCfPaFgHNuXG4pC37_yXpsAfxTcSGmxqeEK2PKlXQSUm7pkYveXn7_kk0rKgdkc5fsLhw2Tvj79Mm3VHRPi4vQCt2lfPTJ5IuvfySsaIdD7nzeR3lWJ3Vl7M0uB25rTYw1hUW6mGZQYnrsQCza8H8GhOs1fgcNMH-2Fb0z_P5JKMprO483RZt_3f_8SZKBbxcKrOuisWo8e-784mn82ZfB8xhw2Z-FdAJIX5koh8M1v_Ap6_qBzAV_cqh30SI3et6PZ1HgNww'})
    pet = resp.json()['animals'][0]


    return pet


# {"token_type":"Bearer","expires_in":3600,"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjUwYzAwNTgxMGI3NmJiYmVmN2JhNDk1ODliNjU4MjNkMzhlNDE4YTBmMzUyODg0OGM1OTMyMGJjMDgyNThlMGE3ODM0YjkyNjc0N2UzNzVjIn0.eyJhdWQiOiJGTVlNbHY0SHZNMVJzYUdRSHg4b1poZEFNaFJGenRlcWJvdWRtdDMzaEZ1VElhZ3VubiIsImp0aSI6IjUwYzAwNTgxMGI3NmJiYmVmN2JhNDk1ODliNjU4MjNkMzhlNDE4YTBmMzUyODg0OGM1OTMyMGJjMDgyNThlMGE3ODM0YjkyNjc0N2UzNzVjIiwiaWF0IjoxNTU1NzE0NDg2LCJuYmYiOjE1NTU3MTQ0ODYsImV4cCI6MTU1NTcxODA4Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.zDtRNYTvNFtkxiPQ03Q6EAuQRg_1LmFyQeLWb_IAIGzkFzL6zp1-ssvFSjRmoFV1Fjc5P1rgZfIKGsCfPaFgHNuXG4pC37_yXpsAfxTcSGmxqeEK2PKlXQSUm7pkYveXn7_kk0rKgdkc5fsLhw2Tvj79Mm3VHRPi4vQCt2lfPTJ5IuvfySsaIdD7nzeR3lWJ3Vl7M0uB25rTYw1hUW6mGZQYnrsQCza8H8GhOs1fgcNMH-2Fb0z_P5JKMprO483RZt_3f_8SZKBbxcKrOuisWo8e-784mn82ZfB8xhw2Z-FdAJIX5koh8M1v_Ap6_qBzAV_cqh30SI3et6PZ1HgNww"}