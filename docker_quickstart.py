""" Quickstart script for InstaPy usage """
# imports
import os
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = os.environ["INSTA_USER"]
insta_password = os.environ["INSTA_PW"]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
suspicious = False

try:
    suspicious = os.environ["INSTA_SUSPICIOUS_BYPASS"]
except:
    print("no suspicious")

if suspicious:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      bypass_suspicious_attempt=True, bypass_with_mobile=True,
                      selenium_local_session=False,
                      use_firefox=True,
                      nogui=True)
else:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      selenium_local_session=False,
                      use_firefox=True,
                      nogui=True)

session.set_selenium_remote_session(
    selenium_url='http://127.0.0.1:4444')
#hashtags = ["familia", "baby", "babylove", "newborn", "bebe", "meubebe", "mamae", "papai", "mae", "pai", "daddy", "dad", "mommy", "mom", "babytips", "children", "instababy", "instababies", "cutebaby", "bebelindo", "filho", "filha", "maternidade", "enxoval", "gravida", "vidademae", "maternidadereal", "maedeprimeiraviagem", "maecoruja", "enxovaldebebe", "crianca", "gestante", "pregnant", "gravidez", "amordemae", "maedeprincesa", "filhos", "maedemenino", "babyboy", "maedemenina"]

hashtags = ["maedeprimeiraviagem", "maecoruja", "enxovaldebebe",
            "gestante", "amordemae", "maedeprincesa", "maedemenino", "maedemenina"]

""" Activity flow """
session.login()

# general settings
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_likes=(
    50, 500), peak_comments=(20, 100), peak_follows=(48, None), peak_unfollows=(35, 400), peak_server_calls=(2000, 15000))

session.set_relationship_bounds(enabled=True,
                                delimit_by_numbers=True,
                                potency_ratio=None,
                                max_followers=10000,
                                min_followers=49,
                                min_following=99,
                                max_following=5000,
                                min_posts=10)

session.set_dont_include(["candreoliveira", "hannacastro"])

session.set_dont_like(["sport", "[soccer", "[cat", "[dog", "[crazy"])

session.set_smart_hashtags(hashtags, limit=10, sort='top', log_tags=True)

session.set_mandatory_words(hashtags)

session.set_delimit_commenting(enabled=True, min=4, comments_mandatory_words=[
                               'maecoruja', 'maedemenino', 'maedeprincesa', 'maedemenina', 'gravida', 'gravidez', 'gravidez', 'newborn', 'babyboy', 'instababy', 'pregnant'])

session.set_skip_users(skip_private=True,
                       private_percentage=90,
                       skip_no_profile_pic=True,
                       skip_business=True)

session.set_dont_unfollow_active_users(enabled=True, posts=50)

session.set_use_meaningcloud(
    enabled=True, license_key=os.environ["MEANINGCLOUD_LIC_KEY"], polarity="P+")

session.set_use_yandex(
    enabled=True, API_key=os.environ["YANDEX_API_KEY"], match_language=True, language_code="pt")

session.set_user_interact(amount=2, percentage=70,
                          randomize=True, media="Photo")
session.set_do_like(enabled=True, percentage=90)

session.set_do_comment(enabled=True, percentage=14)

#session.set_reply_comments(replies=[u"\u2764", u"\u2764", u"\u2764"], media="Photo")
session.set_comments(
    [u":heart: @{}", u":blue_heart: @{}", u":purple_heart: @{}"])

session.set_do_follow(enabled=True, percentage=50, times=2)

# activity
# likes por smart hashtags
session.like_by_tags(amount=100, use_smart_hashtags=True)

# unfollow
session.unfollow_users(amount=100, InstapyFollowed=(
    True, "nonfollowers"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)

# comentarios
session.comment_by_locations(['213163910', '213088533', '213088533', '28288090',
                              '429343414092222', '243676859'], amount=40, skip_top_posts=True)

# likes por feed
session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)

session.end()
