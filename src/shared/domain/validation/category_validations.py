from src.shared.exceptions.domain_exceptions import InvalidCategoryMemberTypeError
from src.shared.domain.contracts import EntityContract

class CategoryValidator:
    def __init__(
            self,
            member_category_types: tuple[type[EntityContract], ...],
            ) -> None:

        self.member_category_types = member_category_types

    def validate_category_member_type(self, member: EntityContract) -> None:
        if not isinstance(member, self.member_category_types):
            message = (
                f"Invalid member type: {type(member)}. "
                f"Allowed types: {', '.join([t.__name__ for t in self.member_category_types])}"
            )
            raise InvalidCategoryMemberTypeError(message)
