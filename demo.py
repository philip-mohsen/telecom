from src.shared.infrastructure.json_db import JSONDatabase
from src.service_catalog.domain.enums import ContentValueType
from src.service_catalog.domain.value_objects import MinuteValue, DataLimitValue
from src.service_catalog.infrastructure.repositories.technology_repository import TechnologyRepository
from src.service_catalog.infrastructure.repositories.technology_service_repository import TechnologyServiceRepository
from src.service_catalog.infrastructure.repositories.country_repository import CountryRepository
from src.product_catalog.infrastructure.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.infrastructure.repositories.product_repository import ProductRepository
from src.service_catalog.application.use_cases.create_technology import CreateTechnologyUseCase
from src.service_catalog.application.use_cases.create_technology_service import CreateTechnologyServiceUseCase
from src.service_catalog.application.use_cases.create_country import CreateCountryUseCase
from src.product_catalog.application.use_cases.create_product_template import CreateProductTemplateUseCase
from src.product_catalog.application.use_cases.create_product import CreateProductUseCase

# Connect to the database
# This is only for demo purposes. In a real-world application, this would a relational database.
db = JSONDatabase(data_dir="tests/data")
db.clear()

# Create mobile technologies
technology_repository = TechnologyRepository(json_db=db)
use_case = CreateTechnologyUseCase(technology_repository=technology_repository)
tech_2g = use_case.execute(name="Global System for Mobile Communication", abbreviation="2G/GSM")
tech_3g = use_case.execute(name="Universal Mobile Telecommunications System", abbreviation="3G/UMTS")
tech_4g = use_case.execute(name="Long-Term Evolution", abbreviation="4G/LTE")
tech_5g = use_case.execute(name="New Radio", abbreviation="5G/NR")

# Create mobile services
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
technology_repository = TechnologyRepository(json_db=db) # refresh the repository
technology_service_repository = TechnologyServiceRepository(json_db=db)

use_case = CreateTechnologyServiceUseCase(
    technology_service_repository=technology_service_repository,
    technology_repository=technology_repository)

mobile_voice_service = use_case.execute(
    name="Mobile Voice Service",
    technology_uuids=[tech_2g.uuid, tech_3g.uuid, tech_4g.uuid, tech_5g.uuid],
    content_value_type=ContentValueType.MINUTE)

mobile_data_service_5g = use_case.execute(
    name = "5G Mobile Data Service",
    technology_uuids=[tech_5g.uuid],
    content_value_type=ContentValueType.DATA_LIMIT)

# Create product template, grouping product content together.
# At this point, the product content is not yet associated with the actual content values.
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
technology_service_repository = TechnologyServiceRepository(json_db=db) # refresh the repository
product_template_repository = ProductTemplateRepository(json_db=db)

use_case = CreateProductTemplateUseCase(
    product_template_repository=product_template_repository,
    technology_service_repository=technology_service_repository)

product_template = use_case.execute(
    name="Unnamed Mobile Plan",
    service_uuids=[
        mobile_voice_service.uuid,
        mobile_data_service_5g.uuid
    ]) # the service_uuids can be extend with collection of value objects holdings counters per each service

# Create country for destinations
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
country_repository = CountryRepository(json_db=db)
use_case = CreateCountryUseCase(country_repository=country_repository)
country_bg = use_case.execute(name="Bulgaria")
country_serbia = use_case.execute(name="Serbia")
country_romania = use_case.execute(name="Romania")

# Create concrete product based on a product template.
# The presentation layer will iterate each product content and ask the user for the actual content values.
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
technology_service_repository = TechnologyServiceRepository(json_db=db) # refresh the repository
product_template_repository = ProductTemplateRepository(json_db=db) # refresh the repository
product_repository = ProductRepository(json_db=db)

use_case = CreateProductUseCase(
    product_repository=product_repository,
    product_template_repository=product_template_repository)

# These values will come from the user interface
low_product_content_values = {
    mobile_voice_service.uuid: MinuteValue(100, location_uuid=country_bg.uuid, destination_uuid=country_bg.uuid),
    mobile_voice_service.uuid: MinuteValue(5, location_uuid=country_bg.uuid, destination_uuid=country_serbia.uuid),
    mobile_voice_service.uuid: MinuteValue(1, location_uuid=country_bg.uuid, destination_uuid=country_romania.uuid),
    mobile_data_service_5g.uuid: DataLimitValue(10)
}

use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (Low)",
    content_values=low_product_content_values)

mid_product_content_values = {
    mobile_voice_service.uuid: MinuteValue(500, location_uuid=country_bg.uuid, destination_uuid=country_bg.uuid),
    mobile_voice_service.uuid: MinuteValue(25, location_uuid=country_bg.uuid, destination_uuid=country_serbia.uuid),
    mobile_voice_service.uuid: MinuteValue(5, location_uuid=country_bg.uuid, destination_uuid=country_romania.uuid),
    mobile_data_service_5g.uuid: DataLimitValue(50)
}

use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (Mid)",
    content_values=mid_product_content_values)

high_product_content_values = {
    mobile_voice_service.uuid: MinuteValue(1000, location_uuid=country_bg.uuid, destination_uuid=country_bg.uuid),
    mobile_voice_service.uuid: MinuteValue(50, location_uuid=country_bg.uuid, destination_uuid=country_serbia.uuid),
    mobile_voice_service.uuid: MinuteValue(10, location_uuid=country_bg.uuid, destination_uuid=country_romania.uuid),
    mobile_data_service_5g.uuid: DataLimitValue(100)
}

use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (High)",
    content_values=high_product_content_values)
