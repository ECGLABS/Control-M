import requests

def trigger_controlm_job():
    url = 'http://controlm_server:port/ctmrest/v1/<domain>/jobs'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Basic base64_encoded_credentials'}
    data = {
        "jobName": "YourJobName",
        "applicationName": "YourApplicationName",
        "folderName": "YourFolderName",
        "runAs": "username"
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Job triggered successfully!")
    else:
        print(f"Error triggering job: {response.text}")

if __name__ == "__main__":
    trigger_controlm_job()
