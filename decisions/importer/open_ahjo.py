# -*- coding: utf-8 -*-
import json

from decisions.models import Action, Case, Content, DataSource, Event, Function, Organization

from .base import Importer


class OpenAhjoImporter(Importer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_source, created = DataSource.objects.get_or_create(
            identifier='open_ahjo',
            defaults={'name': 'Open Ahjo'}
        )
        if created:
            self.logger.debug('Created new data source "open_ahjo"')

    def _import_functions(self, data):
        self.logger.info('Importing functions...')

        for function_data in data['categories']:
            defaults = dict(
                data_source=self.data_source,
                name=function_data['name'],
                function_id=function_data['origin_id'],
            )

            parent_id = function_data['parent']
            if parent_id:
                try:
                    defaults['parent'] = Function.objects.get(origin_id=parent_id)
                except Function.DoesNotExist:
                    self.logger('Function parent %s does not exist' % parent_id)
                    continue

            function, created = Function.objects.update_or_create(
                origin_id=function_data['id'],
                defaults=defaults
            )

            if created:
                self.logger.info('Created function %s' % function)

    def _import_events(self, data):
        self.logger.info('Importing events...')

        # build dict of organizations to make matching policymakers to organizations faster
        organization_dict = {o['policymaker']: o for o in data['organizations'] if o['policymaker']}

        for meeting_data in data['meetings']:
            defaults = dict(
                data_source=self.data_source,
                origin_id=meeting_data['id'],
                start_date=meeting_data['date'],
                end_date=meeting_data['date'],
            )

            organization_data = organization_dict.get(meeting_data['policymaker'])
            if organization_data:
                try:
                    organization = Organization.objects.get(origin_id=organization_data['origin_id'])
                    defaults['organization'] = organization
                except Organization.DoesNotExist:
                    self.logger.error('Organization %s does not exist' % organization_data['origin_id'])
                    continue

            event, created = Event.objects.update_or_create(
                origin_id=meeting_data['id'],
                defaults=defaults
            )

            if created:
                self.logger.info('Created event %s' % event)

    def _import_cases(self, data):
        self.logger.info('Importing cases...')

        for issue_data in data['issues']:
            defaults = dict(
                data_source=self.data_source,
                title=issue_data['subject'],
                register_id=issue_data['register_id'],
            )

            try:
                defaults['function'] = Function.objects.get(origin_id=issue_data['category'])
            except Function.DoesNotExist:
                self.logger.error('Function %s does not exist' % issue_data['category'])
                continue

            case, created = Case.objects.update_or_create(
                origin_id=issue_data['id'],
                defaults=defaults,
            )

            if created:
                self.logger.info('Created case %s' % case)

    def _import_actions(self, data):
        self.logger.info('Importing actions...')

        for agenda_item_data in data['agenda_items']:
            defaults = dict(
                data_source=self.data_source,
                title=agenda_item_data['subject'],
                ordering=agenda_item_data['index'],
                resolution=agenda_item_data['resolution'] or '',
            )
            if agenda_item_data['issue']:
                try:
                    case = Case.objects.get(origin_id=agenda_item_data['issue'])
                    defaults['case'] = case
                except Case.DoesNotExist:
                    self.logger.error('Case %s does not exist' % agenda_item_data['issue'])
                    continue
            try:
                event = Event.objects.get(origin_id=agenda_item_data['meeting'])
                defaults['event'] = event
            except Event.DoesNotExist:
                self.logger.error('Event %s does not exist' % agenda_item_data['meeting'])
                continue

            action, created = Action.objects.update_or_create(
                origin_id=agenda_item_data['id'],
                defaults=defaults
            )

            if created:
                self.logger.info('Created action %s' % action)

    def _import_contents(self, data):
        self.logger.info('Importing contents...')

        for content_section_data in data['content_sections']:
            defaults = dict(
                data_source=self.data_source,
                origin_id=content_section_data['id'],
                hypertext=content_section_data['text'],
                type=content_section_data['type'],
                ordering=content_section_data['index'],
            )

            action_id = content_section_data.get('agenda_item')
            try:
                action = Action.objects.get(origin_id=action_id)
                defaults['action'] = action
            except Action.DoesNotExist:
                self.logger.error('Action %s does not exist' % action_id)
                continue

            content, created = Content.objects.update_or_create(
                origin_id=content_section_data['id'],
                defaults=defaults
            )

            if created:
                self.logger.info('Created content %s' % content)

    def import_data(self, filename):
        self.logger.info('Importing open ahjo data...')
        data_file = open(filename, 'r')
        data = json.load(data_file)
        data_file.close()

        self._import_functions(data)
        self._import_events(data)
        self._import_cases(data)
        self._import_actions(data)
        self._import_contents(data)
