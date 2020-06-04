import json
import requests
import time

#https://chat-api.com/en/swagger.html?utm_source=email&utm_medium=email_doc&utm_campaign=welcome#/messages/sendLink

class WABot():
    def __init__(self):
        # self.json = json
        # self.dict_messages = json['messages']
        self.APIUrl = 'confidencial'
        self.token = 'confidencial'

    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"phone": chatID, "body": text}
        time.sleep(20)
        answer = self.send_requests('sendMessage', data)
        return answer

    def send_link(self, phone, body, preview, title):
        data = {"phone": phone, "body": body, "previewBase64": preview, "title": title}
        answer = self.send_requests('sendLink', data)
        return answer

    def send_image(self, phone, body, filename, caption):
        data = {"phone": phone, "body": body, "filename": filename, "caption": caption}
        time.sleep(30)
        answer = self.send_requests('sendFile', data)
        return answer
