import requests
import json
import base64

filepath="invoice.pdf"

url = "https://api-v2.finovox.com/analyse"
filename=filepath.split('/')[-1]
files=[('file',(filename,open(filepath,'rb')))]
headers = {
  'api-key': 'YOUR_API_KEY'
}
payload = {"analyse_type": [ "risk","data_extraction","pdf_report"]}
payload_string = json.dumps(payload)
response_data = requests.request("POST", url, headers=headers, files=files, data={"payload": payload_string})

result_json = json.loads(response_data.text)
if "pdf_report" in result_json:
    pdf_report = result_json["pdf_report"]
    for language in pdf_report:
        pdf_report[language] = base64.b64decode(pdf_report[language])
        save_path = f"report_{language}.pdf"
        with open(save_path, "wb") as f:
            f.write(pdf_report[language])
        print(f"report_{language}.pdf saved")
    del result_json["pdf_report"]

with open("result.json", "w") as f:
    json.dump(result_json, f, indent=4)
print("result.json saved")