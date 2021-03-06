import datetime
# import the logging library
import logging

# Get an instance of a logger
from PIL import Image, ImageFilter

logger = logging.getLogger('bot.utils.util')


def log(tag, message):
    logger.debug(message)
    log_message = ('%s - %s: %s' % ('{:%H:%M:%S %m-%d-%Y}'.format(datetime.datetime.now()), tag, message))
    print log_message


def log_error(tag, message):
    logger.error(message)
    log_message = ('ERROR: %s - %s: %s' % ('{:%H:%M:%S %m-%d-%Y}'.format(datetime.datetime.now()), tag, message))
    print log_message


def seconds_to_time(seconds):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    days = seconds // seconds_in_day
    seconds -= days * seconds_in_day

    hours = seconds // seconds_in_hour
    seconds -= hours * seconds_in_hour

    minutes = seconds // seconds_in_minute
    seconds -= minutes * seconds_in_minute
    if days > 0:
        return "{0:.0f} days, {1:.0f} hours".format(days, hours)
    elif hours == 23:
        return "24 hours"
    elif hours > 0:
        return "{0:.0f} hours, {1:.0f} minutes".format(hours, minutes)
    elif minutes > 0:
        if minutes < 10:
            return "less then ten minutes"
        if minutes < 60:
            return "less then one hour"
        return "{0:.0f} minutes".format(minutes)


def build_topics(topic_header, topics_set):
    topics = topic_header + " && "
    first = True
    for topic in topics_set:
        if first:
            topics = topics + "('" + topic + "' in topics"
            first = False
        else:
            topics = topics + " || '" + topic + "' in topics"
    topics = topics + ")"
    return topics


def get_fcm_topics_and_onesignal_segments(launch, debug=False, flutter=False, notification_type=None):
    location_id = 0
    segments = ['ALL-Filter']
    topics_set = ['all']
    if flutter:
        if not debug:
            topic_header = "'flutter_production' in topics && '%s' in topics" % notification_type
        else:
            topic_header = "'flutter_debug' in topics && '%s' in topics" % notification_type
    else:
        if not debug:
            topic_header = "'production' in topics"
        else:
            topic_header = "'debug' in topics"

    if launch.location is not None:
        location_id = launch.location.id
    lsp_id = launch.lsp.id

    if lsp_id == 44:
        topics_set.append('nasa')
        segments.append('Nasa')
    if lsp_id == 115:
        topics_set.append('arianespace')
        segments.append('Arianespace')
    if lsp_id == 121:
        topics_set.append('spacex')
        segments.append('SpaceX')
    if lsp_id == 124:
        topics_set.append('ula')
        segments.append('ULA')
    if lsp_id == 111 or lsp_id == 63:
        topics_set.append('roscosmos')
        segments.append('Roscosmos')
    if lsp_id == 88:
        topics_set.append('casc')
        segments.append('CASC')
    if location_id == 16:
        topics_set.append('ksc')
        segments.append('KSC')
    if location_id == 11:
        topics_set.append('ples')
        segments.append('Ples')
    if location_id == 18:
        topics_set.append('van')
        segments.append('Van')
    topics = build_topics(topic_header, topics_set)
    return {'segments': segments, 'topics': topics}


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def drop_shadow(image, offset=(5, 5), background=0xffffff, shadow=0x444444,
               border=8, iterations=5):
    """
    Add a gaussian blur drop shadow to an image.

    image       - The image to overlay on top of the shadow.
    offset      - Offset of the shadow from the image as an (x,y) tuple.  Can be
                  positive or negative.
    background  - Background colour behind the image.
    shadow      - Shadow colour (darkness).
    border      - Width of the border around the image.  This must be wide
                  enough to account for the blurring of the shadow.
    iterations  - Number of times to apply the filter.  More iterations
                  produce a more blurred shadow, but increase processing time.
    """

    # Create the backdrop image -- a box in the background colour with a
    # shadow on it.
    totalWidth = image.size[0] + abs(offset[0]) + 2 * border
    totalHeight = image.size[1] + abs(offset[1]) + 2 * border
    back = Image.new(image.mode, (totalWidth, totalHeight), background)

    # Place the shadow, taking into account the offset from the image
    shadowLeft = border + max(offset[0], 0)
    shadowTop = border + max(offset[1], 0)
    back.paste(shadow, [shadowLeft, shadowTop, shadowLeft + image.size[0],
                        shadowTop + image.size[1]])

    # Apply the filter to blur the edges of the shadow.  Since a small kernel
    # is used, the filter must be applied repeatedly to get a decent blur.
    n = 0
    while n < iterations:
        back = back.filter(ImageFilter.BLUR)
        n += 1

    # Paste the input image onto the shadow backdrop
    imageLeft = border - min(offset[0], 0)
    imageTop = border - min(offset[1], 0)
    back.paste(image, (imageLeft, imageTop))

    return back
