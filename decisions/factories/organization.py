import factory
from faker import Faker
from decisions.models import Organization

fake = Faker()
fake.seed(7)


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = fake.company()
    abstract = fake.paragraph(nb_sentences=1)
    description = fake.paragraph(nb_sentences=5)
    classification = fake.company_suffix()
    founding_date = fake.date()
