from enum import Enum

class ContentValueType(Enum):
    MINUTE = "MinuteValue"
    MESSAGE_COUNT = "MessageCountValue"
    DATA_LIMIT = "DataLimitValue"
    INTERNET_SPEED = "InternetSpeedValue"
    CHANNEL = "ChannelValue"
