# youtube_scraper_dataAPI

This scraper use [YouTube Data API](https://developers.google.com/youtube/v3/docs/channels/list) to retrive the data such as total views, total subscribers and total videos posted.

It uses the id request parameter to identify the channel by its YouTube channel ID.

Change `.env` file with your own API keys obtained from your [Google Cloud Console](https://console.cloud.google.com/) account.

Please change the `channel_id` parameter in `line 22` to channel desired
This example retrieves channel data for the _cs50_ and _freeCodeCamp.org_ YouTube channel.

**note:** _This method only retrieves channel data from channel ID only._

The result is shown in pandas dataFrame. This results can be converted into JSON or CSV format.
![](/result.png)

## Troubleshooting

You can find channel id by putting its username from this [website](https://commentpicker.com/youtube-channel-id.php).

If you tried to retrieve the data via YouTube username using `forUsername` method and it didn't work because only applies to channels with a legacy username.
![](/error.png)

[support article](https://support.google.com/youtube/answer/6180214?hl=en#:~:text=Legacy%20username%20URL&text=Usernames%20are%20no%20longer%20required,usernames%20can%27t%20be%20changed)
