from src.shared.persistence.json_db import JSONDatabase
from src.service_catalog.domain.enums import ContentValueType
from src.service_catalog.domain.value_objects import MinuteValue, DataLimitValue
from src.service_catalog.repositories.technology_repository import TechnologyRepository
from src.service_catalog.repositories.technology_service_repository import TechnologyServiceRepository
from src.product_catalog.repositories.product_content_repository import ProductContentRepository
from src.product_catalog.repositories.product_template_repository import ProductTemplateRepository
from src.product_catalog.repositories.product_repository import ProductRepository
from src.service_catalog.application.use_cases.create_technology import CreateTechnologyUseCase
from src.service_catalog.application.use_cases.create_technology_service import CreateTechnologyServiceUseCase
from src.product_catalog.application.use_cases.create_product_content import CreateProductContentUseCase
from src.product_catalog.application.use_cases.create_producte_template import CreateProductTemplateUseCase
from src.product_catalog.application.use_cases.create_product import CreateProductUseCase

# Connect to the database
# This is only for demo purposes. In a real-world application, this would a relational database.
db = JSONDatabase(data_dir="tests/data")
db.clear()

# Create mobile technologies
technology_repository = TechnologyRepository(json_db=db)
use_case = CreateTechnologyUseCase(technology_repository=technology_repository)
tech_2g = use_case.execute(name="Global System for Mobile Communication", abbreviation="2G/GSM")
tech_3g = use_case.execute(name="Universal MobileTelecommunicationsSystem", abbreviation="3G/UMTS")
tech_4g = use_case.execute(name="Long-Term Evolution", abbreviation="4G/LTE")
tech_5g = use_case.execute(name="New Radio", abbreviation="5G/NR")

# Create mobile services
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
technology_repository = TechnologyRepository(json_db=db)
technology_service_repository = TechnologyServiceRepository(json_db=db) # refresh the repository

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

# Create product content.
# Product content is a just a place holder for the actual content.
# At this point, the product content is not yet associated with the actual content values.
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
technology_service_repository = TechnologyServiceRepository(json_db=db) # refresh the repository
product_content_repository = ProductContentRepository(json_db=db)

use_case = CreateProductContentUseCase(
    product_content_repository=product_content_repository,
    technology_service_repository=technology_service_repository)

national_mobile_voice_minutes = use_case.execute(
    name="National Mobile Voice Minutes",
    service_uuid=mobile_voice_service.uuid)

international_mobile_voice_minutes = use_case.execute(
    name="International Mobile Voice Minutes",
    service_uuid=mobile_voice_service.uuid)

national_mobile_data_limit = use_case.execute(
    name="National Mobile Data Limit",
    service_uuid=mobile_data_service_5g.uuid)

# Create product template, grouping product content together.
# At this point, the product content is not yet associated with the actual content values.
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
product_content_repository = ProductContentRepository(json_db=db) # refresh the repository
product_template_repository = ProductTemplateRepository(json_db=db)

use_case = CreateProductTemplateUseCase(
    product_template_repository=product_template_repository,
    product_content_repository=product_content_repository)

product_template = use_case.execute(
    name="Unnamed Mobile Plan",
    content_uuids=[
        national_mobile_voice_minutes.uuid,
        international_mobile_voice_minutes.uuid,
        national_mobile_data_limit.uuid
    ])

# Create concrete product based on a product template.
# The presentation layer will iterate each product content and ask the user for the actual content values.
# This is only for demo purposes. In a real-world application, this would be done by the user interface.
product_content_repository = ProductContentRepository(json_db=db) # refresh the repository
product_template_repository = ProductTemplateRepository(json_db=db) # refresh the repository
product_repository = ProductRepository(json_db=db)

use_case = CreateProductUseCase(
    product_repository=product_repository,
    product_template_repository=product_template_repository,
    product_content_repository=product_content_repository)

# These values will come from the user interface
low_product_content_values = {
    national_mobile_voice_minutes.uuid: MinuteValue(100),
    international_mobile_voice_minutes.uuid: MinuteValue(10),
    national_mobile_data_limit.uuid: DataLimitValue(10)
}

# These values will come from the user interface
mid_product_content_values = {
    national_mobile_voice_minutes.uuid: MinuteValue(500),
    international_mobile_voice_minutes.uuid: MinuteValue(50),
    national_mobile_data_limit.uuid: DataLimitValue(50)
}

# These values will come from the user interface
high_product_content_values = {
    national_mobile_voice_minutes.uuid: MinuteValue(1000),
    international_mobile_voice_minutes.uuid: MinuteValue(100),
    national_mobile_data_limit.uuid: DataLimitValue(100)
}

low_content_product = use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (Low)",
    content_values=low_product_content_values)

mid_content_product = use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (Mid)",
    content_values=mid_product_content_values)

high_content_product = use_case.execute(
    template_uuid=product_template.uuid,
    product_name="Unnamed Mobile Plan (High)",
    content_values=high_product_content_values)
