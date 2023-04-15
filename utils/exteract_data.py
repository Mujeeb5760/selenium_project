import time

scroll_time = 5


def scroll_to_page_end(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        time.sleep(scroll_time)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def extract_videos_data(soup):
    video_elements = soup.find_all('ytd-rich-item-renderer')
    channel_videos_data = []
    for videos in video_elements:
        title = videos.find('yt-formatted-string', {"id": "video-title"}).text
        views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
        upload_time = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).next
        duration = videos.find('span',
                               {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text.strip()
        thumbnails = videos.find('img', {"style": "background-color: transparent;"}).get('src')
        video_data = {
            "Title": title,
            "Views": views,
            "Upload Time": upload_time,
            "Duration": duration,
            "Thumbnails": thumbnails
        }
        channel_videos_data.append(video_data)
    return channel_videos_data
