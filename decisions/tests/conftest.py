from pytest_factoryboy import register

from decisions.factories import ActionFactory, CaseFactory, EventFactory, FunctionFactory, OrganizationFactory

register(ActionFactory)
register(CaseFactory)
register(FunctionFactory)
register(EventFactory)
register(OrganizationFactory)
