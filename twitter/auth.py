import requests
import os
from loguru import logger
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'


def get_user_id(_ac):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://x.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://x.com/",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "x-client-transaction-id": "Os7a6RTuRN8qd551UcCISYc9Wg633DGC2yJ5qhHIuSudLFQRaLVsSez9GHgTAjpQdCRkrjl2l/IqJoOBAN0fQ6UUpu7mOQ",
        "x-guest-token": "1906551182975545447",
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "zh-cn"
    }

    url = "https://api.x.com/graphql/32pL5BWe9WKeSK1MoPvFQQ/UserByScreenName"
    params = {
        "variables": f"{{\"screen_name\":\"{_ac}\"}}",
        "features": "{\"hidden_profile_subscriptions_enabled\":true,\"profile_label_improvements_pcf_label_in_post_enabled\":true,\"rweb_tipjar_consumption_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"subscriptions_verification_info_is_identity_verified_enabled\":true,\"subscriptions_verification_info_verified_since_enabled\":true,\"highlights_tweets_tab_ui_enabled\":true,\"responsive_web_twitter_article_notes_tab_enabled\":true,\"subscriptions_feature_can_gift_premium\":true,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"responsive_web_graphql_timeline_navigation_enabled\":true}",
        "fieldToggles": "{\"withAuxiliaryUserLabels\":false}"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['data']['user']['result']['rest_id']


if __name__ == '__main__':
    # ac = input("请输入AC：")
    ac = "honkaistarrail"
    user_id = get_user_id(ac)
    logger.info(f"用户ID：{user_id}")