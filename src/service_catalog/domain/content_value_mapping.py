from src.service_catalog.domain.value_objects import MinuteValue
from src.service_catalog.domain.value_objects import DataLimitValue
from src.service_catalog.domain.value_objects import TVPackageValue
from src.service_catalog.domain.enums import ContentValueType

CONTENT_VALUE_MAPPING = {
    ContentValueType.MINUTE: MinuteValue,
    ContentValueType.DATA_LIMIT: DataLimitValue,
    ContentValueType.TV_PACKAGE: TVPackageValue,
}
