"""Converts between Python datetimes and ResoniteLink's DateTime and TimeSpan strings.

ResoniteLink sends both types as strings, in the formats .NET uses:

- DateTime: ISO 8601 with up to seven fractional digits of seconds, e.g.
  ``2024-05-06T07:08:09.1234567Z``. ``Z`` marks a UTC time, and a time
  with no suffix has an unspecified kind. A time sent with an offset, such
  as ``+02:00``, comes back converted to the server's local time.
- TimeSpan: ``[-][d.]hh:mm:ss[.fffffff]``, e.g. ``-1.02:03:04.5000001``
  for minus one day, 2 hours, 3 minutes, and 4.5000001 seconds.

Python keeps microseconds, so the seventh fractional digit, a tick of 100
nanoseconds, is dropped when reading.
"""

import datetime
import re

_DATETIME_RE = re.compile(
    r"^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(?:\.(\d{1,7}))?"
    r"(Z|[+-]\d\d:\d\d)?$"
)
_TIMESPAN_RE = re.compile(
    r"^(-)?(?:(\d+)\.)?(\d\d):(\d\d):(\d\d)(?:\.(\d{1,7}))?$"
)


def _microseconds(fraction: str | None) -> int:
    """Returns the microseconds in a fraction of a second, given its digits.

    Digits past the sixth are dropped, so "1234567" gives 123456.
    """
    if not fraction:
        return 0
    return int(fraction[:6].ljust(6, "0"))


def parse_datetime(text: str) -> datetime.datetime:
    """Returns the datetime in a ResoniteLink DateTime string.

    Args:
        text (str): e.g. "2024-05-06T07:08:09.123Z".

    Returns:
        A datetime in UTC for a "Z" suffix, with a fixed offset for an
        offset suffix, and naive when there's no suffix.

    Raises:
        ValueError: The string isn't in the DateTime format.
    """
    match = _DATETIME_RE.match(text)
    if not match:
        raise ValueError(f"Not a ResoniteLink DateTime: {text!r}")
    year, month, day, hour, minute, second = (int(g) for g in match.groups()[:6])
    suffix = match.group(8)
    tzinfo: datetime.tzinfo | None = None
    if suffix == "Z":
        tzinfo = datetime.timezone.utc
    elif suffix:
        sign = -1 if suffix[0] == "-" else 1
        offset = datetime.timedelta(hours=int(suffix[1:3]), minutes=int(suffix[4:6]))
        tzinfo = datetime.timezone(sign * offset)
    return datetime.datetime(
        year, month, day, hour, minute, second,
        _microseconds(match.group(7)), tzinfo=tzinfo,
    )


def format_datetime(value: datetime.datetime) -> str:
    """Returns the ResoniteLink DateTime string for a datetime.

    An aware datetime is sent as UTC with a "Z" suffix. A naive one is sent
    without a suffix, which the server stores with an unspecified kind.

    Args:
        value (datetime.datetime): The datetime to send.

    Returns:
        e.g. "2024-05-06T07:08:09.123Z".
    """
    suffix = ""
    if value.tzinfo is not None and value.utcoffset() is not None:
        value = value.astimezone(datetime.timezone.utc)
        suffix = "Z"
    text = value.strftime("%Y-%m-%dT%H:%M:%S")
    if value.microsecond:
        text += f".{value.microsecond:06d}".rstrip("0")
    # strftime pads years below 1000 inconsistently across platforms, so
    # the year is formatted separately.
    return f"{value.year:04d}{text[text.index('-'):]}{suffix}"


def parse_timespan(text: str) -> datetime.timedelta:
    """Returns the timedelta in a ResoniteLink TimeSpan string.

    Args:
        text (str): e.g. "-1.02:03:04.5000001".

    Returns:
        The timedelta.

    Raises:
        ValueError: The string isn't in the TimeSpan format.
    """
    match = _TIMESPAN_RE.match(text)
    if not match:
        raise ValueError(f"Not a ResoniteLink TimeSpan: {text!r}")
    negative, days, hours, minutes, seconds, fraction = match.groups()
    magnitude = datetime.timedelta(
        days=int(days or 0), hours=int(hours), minutes=int(minutes),
        seconds=int(seconds), microseconds=_microseconds(fraction),
    )
    return -magnitude if negative else magnitude


def format_timespan(value: datetime.timedelta) -> str:
    """Returns the ResoniteLink TimeSpan string for a timedelta.

    Args:
        value (datetime.timedelta): The duration to send.

    Returns:
        e.g. "-1.02:03:04.5000000".
    """
    # A negative timedelta is stored as negative days plus positive
    # seconds, so the sign is taken off before splitting it up.
    sign = "-" if value < datetime.timedelta(0) else ""
    magnitude = abs(value)
    hours, rest = divmod(magnitude.seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    text = f"{sign}{magnitude.days}." if magnitude.days else sign
    text += f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    if magnitude.microseconds:
        text += f".{magnitude.microseconds * 10:07d}"
    return text
