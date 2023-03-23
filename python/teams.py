import requests
import json
import traceback


def send_message(url, title, text):
    try:
        payload_dic = {
            "title": title,
            "text": text,
        }
        response = requests.post(
            url,
            data=json.dumps(payload_dic)
        )

        return response

    except:
        raise Exception(traceback.format_exc())
