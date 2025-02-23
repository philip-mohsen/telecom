from src.service_catalog.domain.value_objects import MinuteValue
from src.service_catalog.domain.value_objects import MessageCountValue
from src.service_catalog.domain.value_objects import DataLimitValue
from src.service_catalog.domain.value_objects import InternetSpeedValue
from src.service_catalog.domain.value_objects import TVPackageValue
from src.service_catalog.domain.enums import ContentValueType

CONTENT_VALUE_MAPPING = {
    ContentValueType.MINUTE: MinuteValue,
    ContentValueType.MESSAGE_COUNT: MessageCountValue,
    ContentValueType.DATA_LIMIT: DataLimitValue,
    ContentValueType.INTERNET_SPEED: InternetSpeedValue,
    ContentValueType.TV_PACKAGE: TVPackageValue,
}
