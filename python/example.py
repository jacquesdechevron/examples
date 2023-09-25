import requests
filepath="sample.pdf"

url = "https://api-v2.finovox.com/analyse"
filename=filepath.split('/')[-1]
files=[('file',(filename,open(filepath,'rb')))]
headers = {
  'api-key': 'YOUR_API_KEY'
}
response = requests.request("POST", url, headers=headers, files=files)
print(response.text)