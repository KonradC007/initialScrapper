import requests
import random
import re


def process_video(channel):
    try:
        if "https://" in channel['channel']:

            html = requests.get(channel['channel'] + "/about",
                                cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(
                                    random.randint(100, 999))})

        else:
            html = requests.get("https://" + channel['channel'] + "/about",
                                cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(
                                    random.randint(100, 999))})

        subscribers = re.findall(r'(?<=simpleText":").*?(?="})',
                              re.findall(r'(?<=subscriberCountText).*?(?=tvBanner)', html.text)[0])

        description = re.findall(r'(?<=name="description" content=").*?(?="><meta)', html.text)

        channel["subscribers"] = subscribers[0].rsplit('\xa0', 1)[0]
        channel["description"] = description[0]

        print(channel)
        return channel
    except:
        try:
            subscribers = re.findall(r'(?<=simpleText":").*?(?="})',
                                  re.findall(r'(?<=subscriberCountText).*?(?=trackingParams)', html.text)[0])
            channel["subscribers"] = subscribers[0].rsplit('\xa0', 1)[0]

            print(channel)
            return channel
        except:
            print(channel)
            return channel
