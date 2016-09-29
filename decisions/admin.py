from django.apps import apps
from django.contrib import admin
from decisions.models import Membership, Organization, Person


class PersonMembershipInline(admin.TabularInline):
    fields = ('organization', 'role', 'start_date', 'end_date')
    raw_id_fields = ('organization',)
    model = Membership
    extra = 0


class OrganizationMembershipInline(admin.TabularInline):
    fields = ('person', 'role', 'start_date', 'end_date')
    raw_id_fields = ('person',)
    model = Membership
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ('name',)
    inlines = (PersonMembershipInline,)
    search_fields = ('name',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    ordering = ('name',)
    inlines = (OrganizationMembershipInline,)
    search_fields = ('name',)


for model in apps.get_app_config("decisions").get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
