import json
from django.db import migrations 

def add_tour_data(apps,schema_editor):
    Tour = apps.get_model("tours", "Tour")
    data = [
        {
            "title": "Grand Canyon Adventure",
            "city": "Phoenix",
            "price": "299.99",
            "photo": "tour-images/grand-canyon.jpg",
            "address": "123 Canyon Rd, Phoenix, AZ",
            "distance": 10,
            "max_group_size": 15,
            "desc": "Experience the breathtaking views of the Grand Canyon on this guided tour.",
            "featured": True,
        },
        {
            "title": "Paris City Tour",
            "city": "Paris",
            "price": "499.99",
            "photo": "tour-images/paris-city.jpg",
            "address": "456 Champs-Élysées, Paris, France",
            "distance": 5,
            "max_group_size": 20,
            "desc": "Discover the beauty and history of Paris with this exciting city tour.",
            "featured": False,
        },
        {
            "title": "Tokyo Cultural Experience",
            "city": "Tokyo",
            "price": "349.99",
            "photo": "tour-images/tokyo-cultural.jpg",
            "address": "789 Shibuya, Tokyo, Japan",
            "distance": 8,
            "max_group_size": 12,
            "desc": "Immerse yourself in the vibrant culture of Tokyo with this unique tour.",
            "featured": True,
        },
        {
            "title": "New York Skyline Tour",
            "city": "New York",
            "price": "399.99",
            "photo": "tour-images/ny-skyline.jpg",
            "address": "101 Times Square, New York, NY",
            "distance": 7,
            "max_group_size": 25,
            "desc": "Enjoy stunning views of the New York City skyline on this memorable tour.",
            "featured": False,
        },
        {
            "title": "Sydney Harbour Cruise",
            "city": "Sydney",
            "price": "279.99",
            "photo": "tour-images/sydney-harbour.jpg",
            "address": "202 Harbour Rd, Sydney, Australia",
            "distance": 6,
            "max_group_size": 30,
            "desc": "Experience the stunning beauty of Sydney Harbour on this relaxing cruise.",
            "featured": True,
        },
        {
            "title": "Rome Historical Tour",
            "city": "Rome",
            "price": "359.99",
            "photo": "tour-images/rome-historical.jpg",
            "address": "303 Colosseum, Rome, Italy",
            "distance": 4,
            "max_group_size": 18,
            "desc": "Explore the ancient history of Rome with this comprehensive historical tour.",
            "featured": False,
        },
        {
            "title": "London Eye Experience",
            "city": "London",
            "price": "259.99",
            "photo": "tour-images/london-eye.jpg",
            "address": "404 London Eye, London, UK",
            "distance": 3,
            "max_group_size": 10,
            "desc": "Enjoy panoramic views of London from the iconic London Eye.",
            "featured": True,
        },
        {
            "title": "Bangkok Temples Tour",
            "city": "Bangkok",
            "price": "319.99",
            "photo": "tour-images/bangkok-temples.jpg",
            "address": "505 Wat Arun, Bangkok, Thailand",
            "distance": 12,
            "max_group_size": 20,
            "desc": "Visit the stunning temples of Bangkok and learn about Thai culture.",
            "featured": False,
        },
        {
            "title": "Barcelona Beach Tour",
            "city": "Barcelona",
            "price": "229.99",
            "photo": "tour-images/barcelona-beach.jpg",
            "address": "606 Barceloneta Beach, Barcelona, Spain",
            "distance": 9,
            "max_group_size": 25,
            "desc": "Relax and enjoy the sun on the beautiful beaches of Barcelona.",
            "featured": True,
        },
        {
            "title": "Cape Town Wine Tour",
            "city": "Cape Town",
            "price": "399.99",
            "photo": "tour-images/cape-town-wine.jpg",
            "address": "909 Wine Estate Rd, Cape Town, South Africa",
            "distance": 11,
            "max_group_size": 18,
            "desc": "Explore the beautiful vineyards and enjoy wine tasting in Cape Town.",
            "featured": False,
        },
        {
            "title": "Istanbul City Highlights",
            "city": "Istanbul",
            "price": "319.99",
            "photo": "tour-images/istanbul-highlights.jpg",
            "address": "1010 Sultanahmet, Istanbul, Turkey",
            "distance": 6,
            "max_group_size": 22,
            "desc": "Discover the rich history and culture of Istanbul with this comprehensive tour.",
            "featured": True,
        },
    ]

    for tour in data:
        Tour.objects.create(**tour)


class Migration(migrations.Migration):

    dependencies = [
        (
            "tours",
            "0007_tour_tour_id",
        ),
    ]

    operations = [
        migrations.RunPython(add_tour_data),
    ]
