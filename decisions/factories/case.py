import factory
from faker import Faker
from decisions.models import Action, Case, Category

fake = Faker()
fake.seed(7)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = fake.text(max_nb_chars=20)


class CaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Case

    title = fake.text(max_nb_chars=50)
    summary = fake.paragraph(nb_sentences=5)
    register_id = factory.Sequence(lambda n: 'HEL 2016-{:0>6}'.format(n))
    creation_date = fake.date()
    category = factory.SubFactory(CategoryFactory)


class ActionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Action

    title = fake.text(max_nb_chars=50)
    case = factory.SubFactory(CaseFactory)
    resolution = 'proposed'
    ordering = factory.Sequence(lambda n: n)
