from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_customer_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_producttype_fixture.json")
        call_command("loaddata", "db_prod_specification_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_prod_spec_fixture.json")
        call_command("loaddata", "db_productimage_fixture.json")
