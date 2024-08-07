import requests
import datetime as dt
PASSWORD  = "Girgis2004"
USER_NAME = "girgis"



pixel_endpoint = "https://pixe.la/v1/users"

paramaters = {
       "token":PASSWORD,
       "username":USER_NAME,
       "agreeTermsOfService":"yes",
       "notMinor":"yes"
}


# res  = requests.post(pixel_endpoint , json=paramaters)
# print(res.status_code)


post_url = f"{pixel_endpoint}/{USER_NAME}/graphs"

parameters2 = {
       "id":"graph1",
       "name":"Reading Graph",
       "unit":"Pages",
       "type":"int",
       "color":"sora",
}
header = {"X-USER-TOKEN":PASSWORD}

# res = requests.post(url=post_url , json=parameters2,headers=header)
# print(res.text)





post_pexil = f"{pixel_endpoint}/{USER_NAME}/graphs/graph1"
now = dt.datetime.now().strftime("%Y%m%d")
print(now)

body = {
       
       "date":str(now),
       "quantity":input("How many Pages you read ToDay? : "),
       
}



res = requests.post(post_pexil, json=body  ,headers=header)
print(res.text)


update_pexil_url = f"{pixel_endpoint}/{USER_NAME}/graphs/graph1/{str(now)}"


# res = requests.put(url=update_pexil_url,json={"quantity":"30"} , headers=header)
# print(res.text)

delete_pixel_url = f"{pixel_endpoint}/{USER_NAME}/graphs/graph1/{str(now)}"


# res = requests.delete(url=delete_pixel_url , headers=header)
# print(res.text)