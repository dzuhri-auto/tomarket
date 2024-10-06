import json
from datetime import datetime, timedelta, timezone
from urllib.parse import unquote
from tzlocal import get_localzone
from bot.config import settings
from bot.exceptions import MissingApiKeyException


def convert_datetime_str_to_utc(datetime_str):
    decimal_index = datetime_str.find(".")
    if decimal_index != -1:
        # Ensure only 3 digits after the decimal point for milliseconds
        datetime_str = datetime_str[: decimal_index + 4]

    return datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


def format_duration(seconds):
    message = ""
    duration_td = timedelta(seconds=seconds)
    days, day_remainder = divmod(duration_td.total_seconds(), 86400)
    hours, remainder = divmod(day_remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days:
        message = f"{int(days)} days "

    if hours:
        message = message + f"{int(hours)} hours "

    if minutes:
        message = message + f"{int(minutes)} minutes "

    if seconds:
        message = message + f"{int(seconds)} seconds"
    return message.strip()


def remove_query_id_from_tg_web_data(tg_web_data):
    data_to_be_splitted = tg_web_data
    splitted_original_data = data_to_be_splitted.split("&")
    return "&".join(splitted_original_data[1:])


def mapping_role_color(role):
    if role == "admin":
        role = f"<lg>{role}</lg>"
    elif role == "premium":
        role = f"<lc>{role}</lc>"

    return role


def decode_query_id(query_id):
    query_string = query_id
    parameters = query_string.split("&")
    decoded_pairs = [(param.split("=")[0], unquote(param.split("=")[1])) for param in parameters]
    result = dict()
    for key, value in decoded_pairs:
        result[key] = value

    reassign(result)
    return result


def reassign(d):
    """
    check if you have a dict after using literal_eval and reassign
    """
    for k, v in d.items():
        if v[0] in {"{", "["}:
            try:
                evald = json.loads(v)
                if isinstance(evald, dict):
                    d[k] = evald
            except ValueError as err:
                pass


async def get_query_ids():
    temp_lines = []
    with open("query_ids.txt", "r") as file:
        temp_lines = file.readlines()

    lines = [line.strip() for line in temp_lines]
    return lines


def get_tele_obj_from_query_id(query_id):
    tele_obj = decode_query_id(query_id)
    return tele_obj


def convert_to_local_and_unix(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    local_dt = dt.astimezone(get_localzone())
    unix_time = int(local_dt.timestamp())
    return unix_time


def format_large_number(number):
    if number >= 1_000_000_000:  # Check if the number is in billions
        return f"{number / 1_000_000_000:.2f}B"
    elif number >= 1_000_000:  # Check if the number is in millions
        return f"{number / 1_000_000:.2f}M"
    else:
        return str(number)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def check_license_key():
    if not settings.LICENSE_KEY:
        raise MissingApiKeyException("LICENSE KEY is missing, please check your .env file!")
