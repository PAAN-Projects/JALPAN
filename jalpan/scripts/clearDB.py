from management.models import Food


def run():
    Food.objects.all().delete()
