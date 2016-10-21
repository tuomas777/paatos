from pytest_factoryboy import register

from decisions.factories import ActionFactory, CaseFactory, CategoryFactory, EventFactory, OrganizationFactory

register(ActionFactory)
register(CaseFactory)
register(CategoryFactory)
register(EventFactory)
register(OrganizationFactory)
