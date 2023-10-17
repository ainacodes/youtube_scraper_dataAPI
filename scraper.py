from dotenv import load_dotenv
import os
import pandas as pd

import googleapiclient.discovery
import googleapiclient.errors

load_dotenv()

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv('API_KEY')

    channel_id = ['UCcabW7890RKJzL968QWEykA', 'UC8butISFwT-Wl7EV0hUK0BQ']
    channel_id_str = ','.join(channel_id)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id_str
    )

    response = request.execute()

    all_data = []

    for i in range(len(channel_id)):
        title = response['items'][i]['snippet']['title']
        total_views = response['items'][i]['statistics']['viewCount']
        total_subscriber = response['items'][i]['statistics']['subscriberCount']
        total_video = response['items'][i]['statistics']['videoCount']

        data = dict(title=title, total_views=total_views,
                    total_subscriber=total_subscriber, total_video=total_video)

        all_data.append(data)

    df = pd.DataFrame(all_data)

    print(df)


if __name__ == "__main__":
    main()
