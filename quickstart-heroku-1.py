#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Quickstart script for InstaPy usage """
# imports
import sys
import signal
import os
import time
from dotenv import load_dotenv
import threading
from instapy import InstaPy
from instapy.util import smart_run
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))


def task():
    # login credentials
    insta_username = os.environ["INSTA_USER"]
    insta_password = os.environ["INSTA_PW"]

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    suspicious = False
    nogui = True
    use_firefox = True

    try:
        suspicious = os.environ["INSTA_SUSPICIOUS_BYPASS"] in [
            'TRUE', 'T', 't', 'true', 'True', 'Y', 'y', 'YES', 'Yes', 'yes']
        print("INSTA_SUSPICIOUS_BYPASS=" + str(suspicious))
    except:
        print("INSTA_SUSPICIOUS_BYPASS=" + str(suspicious))

    try:
        nogui = os.environ["INSTA_NOGUI"] in ['TRUE', 'T',
                                              't', 'true', 'True', 'Y', 'y', 'YES', 'Yes', 'yes']
        print("INSTA_NOGUI=" + str(nogui))
    except:
        print("INSTA_NOGUI=" + str(nogui))

    try:
        use_firefox = os.environ["INSTA_FIREFOX"] in [
            'TRUE', 'T', 't', 'true', 'True', 'Y', 'y', 'YES', 'Yes', 'yes']
        print("INSTA_FIREFOX=" + str(use_firefox))
    except:
        print("INSTA_FIREFOX=" + str(use_firefox))

    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      bypass_suspicious_attempt=suspicious,
                      bypass_with_mobile=suspicious,
                      use_firefox=use_firefox,
                      disable_image_load=True,
                      nogui=nogui)

    with smart_run(session):
        # hashtags = ["maedeprimeiraviagem", "maecoruja", "enxovaldebebe", "gravidez", "bebe",
        #             "gestante", "amordemae", "maedeprincesa", "maedemenino", "maedemenina"]

        hashtags = ["familia", "baby", "babylove", "newborn", "bebe", "meubebe", "mamae", "papai", "mae", "pai", "daddy", "dad", "mommy", "mom", "babytips", "children", "instababy", "instababies", "cutebaby", "bebelindo", "filho", "filha",
                    "maternidade", "enxoval", "gravida", "vidademae", "maternidadereal", "maedeprimeiraviagem", "maecoruja", "enxovaldebebe", "crianca", "gestante", "pregnant", "gravidez", "amordemae", "maedeprincesa", "filhos", "maedemenino", "babyboy", "maedemenina"]
        accounts = ["paisefilhosoficial", "gravidasonline", "maedeprimeiraviagemdicas",
                    "maeforadacaixa", "graodegente"]
        comments = [u"♥ @{}", u"♥♥♥ @{}", u"♡♡♡ @{}"]
        locations = ['213163910', '213088533', '213088533', '28288090',
                     '429343414092222', '243676859']

        """ Activity flow """
        # general settings
        # peak_server_calls = (3000, 10000)
        session.set_quota_supervisor(enabled=True,
                                     sleep_after=[
                                         "likes_d", "comments_d", "follows_d", "unfollows_d", "server_calls_d"],
                                     sleepyhead=True,
                                     stochastic_flow=True,
                                     notify_me=True,
                                     peak_likes=(45, 1000),
                                     peak_comments=(10, 200),
                                     peak_follows=(80, 1000),
                                     peak_unfollows=(80, 1000))

        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        potency_ratio=1.0,
                                        max_followers=1000000,
                                        min_followers=50,
                                        min_following=50,
                                        max_following=5000,
                                        min_posts=10)

        session.set_dont_include(["candreoliveira", "hannacastro"])

        session.set_dont_like(["futebol", "sport", "soccer", "#cat", "[gat", "[cachorr", "[safad"
                               "[dog", "[crazy", "]sex", "adulto"])

        # session.set_smart_hashtags(hashtags, limit=10, sort='top', log_tags=True)
        # session.set_mandatory_words(hashtags)

        # session.set_delimit_commenting(
        #     enabled=True, min=1, comments_mandatory_words=hashtags)

        # session.set_skip_users(skip_private=False,
        #                        private_percentage=80,
        #                        skip_no_profile_pic=True,
        #                        skip_business=False)

        # session.set_dont_unfollow_active_users(enabled=True, posts=5)

        # session.set_use_meaningcloud(
        #     enabled=False, license_key=os.environ["MEANINGCLOUD_LIC_KEY"], polarity="P+")

        # session.set_use_yandex(
        #     enabled=False, API_key=os.environ["YANDEX_API_KEY"], match_language=True, language_code="pt")

        session.set_user_interact(
            amount=3, percentage=50, randomize=True, media='Photo')

        session.follow_commenters(accounts, amount=100,
                                  daysold=365, max_pic=100, sleep_delay=600, interact=True)

        session.set_do_like(enabled=True, percentage=30)

        session.set_do_follow(enabled=True, percentage=60)

        session.set_do_comment(enabled=True, percentage=90)
        session.set_comments(comments)

        session.set_do_reply_to_comments(enabled=True, percentage=80)
        session.set_comment_replies(replies=comments)

        # activity
        session.comment_by_locations(
            locations, amount=10, skip_top_posts=False)

        session.like_by_locations(locations, amount=100, skip_top_posts=False)

        session.interact_by_comments(usernames=accounts, posts_amount=10,
                                     comments_per_post=3, reply=True, interact=True, randomize=True)

        session.like_by_tags(hashtags, amount=100, use_smart_hashtags=False)

        session.like_by_feed(amount=15, randomize=True,
                             unfollow=True, interact=False)

        session.unfollow_users(amount=1000, nonFollowers=True,
                               style="RANDOM", unfollow_after=48*60*60, sleep_delay=180)


if __name__ == '__main__':
    task()
