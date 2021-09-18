import os
import random
# this is the program to add fake data two models :) using faker module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

## Fake pop script

from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # fake details
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create a new webpage of that topic
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a new access record for above webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # webpg.save()
        # acc_rec.save()


if __name__ == '__main__':
    print("Populating Script")
    populate(10)
    print("populating complete")
