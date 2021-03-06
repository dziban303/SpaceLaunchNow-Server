import pytz
from num2words import num2words

from bot.app.digest.sender import send_twitter_update
from bot.app.repository.launches_repository import *
# import the logging library

# Get an instance of a logger
logger = logging.getLogger('bot.digest')


def check_launch_weekly(DEBUG=True):
    this_weeks_confirmed_launches = []
    this_weeks_possible_launches = []
    repository = LaunchRepository()
    try:
        for launch in repository.get_next_weeks_launches():
            update_notification_record(launch)
            if launch.status == 1 and launch.netstamp > 0:
                this_weeks_confirmed_launches.append(launch)
            elif launch.status == 0 or launch.netstamp == 0:
                this_weeks_possible_launches.append(launch)
        build_weekly_message(this_weeks_possible_launches, this_weeks_confirmed_launches, DEBUG)
    except TypeError as e:
        logger.error(e)


def build_weekly_message(possible, confirmed, DEBUG=True):
    logger.info("Total launches found - confirmed: %s possible: %s" % (len(confirmed), len(possible)))
    full_header = "This Week in SpaceFlight:"
    compact_header = "TWSF:"
    total = (len(possible) + len(confirmed))
    response_id = None

    # First, send out a summary.
    if total == 0:
        message = "%s There are no launches scheduled this week. Follow along with schedule updates at" \
                  " https://spacelaunchnow.me/launches/" % full_header
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) == 1 and len(possible) == 1:
        message = "%s There is one confirmed launch with one other possible this week." % full_header
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) == 0 and len(possible) == 1:
        message = "%s There is one possible launch this week." % full_header
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) == 1 and len(possible) == 0:
        message = "%s There is one confirmed launch this week." % full_header
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) > 1 and len(possible) == 1:
        message = "%s There are %s launches confirmed with one other possible this week." % (full_header,
                                                                                             num2words(
                                                                                                 len(confirmed)))
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) == 1 and len(possible) > 1:
        message = "%s There is one launch confirmed with %s other possible this week." % (full_header,
                                                                                          num2words(len(possible)))
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) > 0 and len(possible) == 0:
        message = "%s There are %s confirmed launches scheduled this week." % (full_header,
                                                                               num2words(len(confirmed)))
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) == 0 and len(possible) > 0:
        message = "%s There are %s possible launches scheduled this week." % (full_header,
                                                                              num2words(len(possible)))
        response_id = send_twitter_update(message, DEBUG, response_id)

    if len(confirmed) == 1:
        launch = confirmed[0]
        day = datetime.fromtimestamp(int(launch.netstamp)).replace(tzinfo=pytz.UTC).strftime("%A")
        message = "%s %s launching from %s on %s. (1/%i)" % (
            compact_header, launch.name, launch.location.name, day,
            total)
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(confirmed) > 1:
        for index, launch in enumerate(confirmed, start=1):
            message = "%s %s launching from %s on %s. (%i/%i)" % (compact_header, launch.name,
                                                                  launch.location.name,
                                                                  datetime
                                                                  .fromtimestamp(int(launch.netstamp))
                                                                  .replace(tzinfo=pytz.UTC)
                                                                  .strftime("%A"),
                                                                  index,
                                                                  total)
            response_id = send_twitter_update(message, DEBUG, response_id)
    if len(possible) == 1:
        launch = possible[0]
        message = "%s %s might launch this week from %s. (%i/%i)" % (compact_header, launch.name,
                                                                     launch.location.name,
                                                                     len(confirmed) + 1, total)
        response_id = send_twitter_update(message, DEBUG, response_id)
    elif len(possible) > 1:
        for index, launch in enumerate(possible, start=1):
            message = "%s %s might be launching from %s. (%i/%i)" % (compact_header,
                                                                     launch.name,
                                                                     launch.location.name,
                                                                     index + len(confirmed),
                                                                     total)
            response_id = send_twitter_update(message, DEBUG, response_id)
