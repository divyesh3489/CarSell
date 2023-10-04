import json
from django.core.management.base import BaseCommand
from Cardata.models import Carbrand, Carmodel


class Command(BaseCommand):
    help = 'Insert data into Django models from JSON'

    def handle(self, *args, **options):
        data = [
            {
                "brand": "Maruti Suzuki",
                "models": [
                    {
                        "model": "WagonR",
                        "mileage": "20.52 kmpl",
                        "doors": 5,
                        "power": "67 bhp @ 6,000 rpm",
                        "boot_space": "341 liters",
                        "seating_capacity": 5,
                        "max_torque": "90 Nm @ 3,500 rpm"
                    },
                    {
                        "model": "Swift",
                        "mileage": "23.2 kmpl",
                        "doors": 5,
                        "power": "82 bhp @ 6,000 rpm",
                        "boot_space": "268 liters",
                        "seating_capacity": 5,
                        "max_torque": "113 Nm @ 4,200 rpm"
                    },
                    {
                        "model": "Baleno",
                        "mileage": "21.01 kmpl",
                        "doors": 5,
                        "power": "82 bhp @ 6,000 rpm",
                        "boot_space": "339 liters",
                        "seating_capacity": 5,
                        "max_torque": "113 Nm @ 4,200 rpm"
                    },
                    {
                        "model": "Alto",
                        "mileage": "22.05 kmpl",
                        "doors": 5,
                        "power": "47 bhp @ 6,000 rpm",
                        "boot_space": "177 liters",
                        "seating_capacity": 5,
                        "max_torque": "69 Nm @ 3,500 rpm"
                    },
                    {
                        "model": "Ciaz",
                        "mileage": "20.04 kmpl",
                        "doors": 4,
                        "power": "103 bhp @ 6,000 rpm",
                        "boot_space": "510 liters",
                        "seating_capacity": 5,
                        "max_torque": "138 Nm @ 4,400 rpm"
                    },
                    {
                        "model": "Ertiga",
                        "mileage": "26.08 kmpl",
                        "doors": 5,
                        "power": "103 bhp @ 6,000 rpm",
                        "boot_space": "209 liters",
                        "seating_capacity": 7,
                        "max_torque": "138 Nm @ 4,400 rpm"
                    }
                ]
            },
            {
                "brand": "Hyundai",
                "models": [
                    {
                        "model": "i20",
                        "mileage": "20.35 kmpl",
                        "doors": 5,
                        "power": "81 bhp @ 6,000 rpm",
                        "boot_space": "311 liters",
                        "seating_capacity": 5,
                        "max_torque": "115 Nm @ 4,000 rpm"
                    },
                    {
                        "model": "Creta",
                        "mileage": "21.4 kmpl",
                        "doors": 5,
                        "power": "138 bhp @ 6,000 rpm",
                        "boot_space": "433 liters",
                        "seating_capacity": 5,
                        "max_torque": "242 Nm @ 1,500-3,200 rpm"
                    },
                    {
                        "model": "Verna",
                        "mileage": "25.0 kmpl",
                        "doors": 4,
                        "power": "113 bhp @ 4,000 rpm",
                        "boot_space": "480 liters",
                        "seating_capacity": 5,
                        "max_torque": "250 Nm @ 1,500-2,750 rpm"
                    },
                    {
                        "model": "Santro",
                        "mileage": "20.3 kmpl",
                        "doors": 5,
                        "power": "68 bhp @ 5,500 rpm",
                        "boot_space": "235 liters",
                        "seating_capacity": 5,
                        "max_torque": "99 Nm @ 4,500 rpm"
                    },
                    {
                        "model": "Venue",
                        "mileage": "17.52 kmpl",
                        "doors": 5,
                        "power": "118 bhp @ 6,000 rpm",
                        "boot_space": "350 liters",
                        "seating_capacity": 5,
                        "max_torque": "172 Nm @ 1,500-4,000 rpm"
                    },
                    {
                        "model": "Tucson",
                        "mileage": "15.38 kmpl",
                        "doors": 5,
                        "power": "152 bhp @ 6,200 rpm",
                        "boot_space": "513 liters",
                        "seating_capacity": 5,
                        "max_torque": "192 Nm @ 4,000 rpm"
                    }
                ]
            },
            {
                "brand": "Mahindra",
                "models": [
                    {
                        "model": "Scorpio",
                        "mileage": "16.36 kmpl",
                        "doors": 5,
                        "power": "138 bhp @ 3,750 rpm",
                        "boot_space": "500 liters",
                        "seating_capacity": 7/9,
                        "max_torque": "320 Nm @ 1,500-2,800 rpm"
                    },
                    {
                        "model": "XUV500",
                        "mileage": "15.1 kmpl",
                        "doors": 5,
                        "power": "153 bhp @ 3,750 rpm",
                        "boot_space": "93 liters",
                        "seating_capacity": 7,
                        "max_torque": "360 Nm @ 1,750-2,800 rpm"
                    },
                    {
                        "model": "Thar",
                        "mileage": "15.2 kmpl",
                        "doors": 3,
                        "power": "150 bhp @ 5,000 rpm",
                        "boot_space": "190 liters",
                        "seating_capacity": 4,
                        "max_torque": "300 Nm @ 1,250-3,000 rpm"
                    },
                    {
                        "model": "Bolero",
                        "mileage": "16.7 kmpl",
                        "doors": 5,
                        "power": "74 bhp @ 3,600 rpm",
                        "boot_space": "384 liters",
                        "seating_capacity": 7,
                        "max_torque": "210 Nm @ 1,600-2,200 rpm"
                    },
                    {
                        "model": "Marazzo",
                        "mileage": "17.3 kmpl",
                        "doors": 4,
                        "power": "121 bhp @ 3,500 rpm",
                        "boot_space": "190 liters",
                        "seating_capacity": 7,
                        "max_torque": "300 Nm @ 1,750-2,500 rpm"
                    },
                    {
                        "model": "KUV100",
                        "mileage": "18.15 kmpl",
                        "doors": 4,
                        "power": "82 bhp @ 5,500 rpm",
                        "boot_space": "243 liters",
                        "seating_capacity": 6,
                        "max_torque": "115 Nm @ 3,500-3,600 rpm"
                    }
                ]
            },
            {
                "brand": "Tata",
                "models": [
                    {
                        "model": "Nexon",
                        "mileage": "21.5 kmpl",
                        "doors": 4,
                        "power": "118 bhp @ 5,500 rpm",
                        "boot_space": "350 liters",
                        "seating_capacity": 5,
                        "max_torque": "170 Nm @ 1,750-4,000 rpm"
                    },
                    {
                        "model": "Tiago",
                        "mileage": "23.84 kmpl",
                        "doors": 4,
                        "power": "84 bhp @ 6,000 rpm",
                        "boot_space": "242 liters",
                        "seating_capacity": 5,
                        "max_torque": "113 Nm @ 3,300 rpm"
                    },
                    {
                        "model": "Harrier",
                        "mileage": "16.35 kmpl",
                        "doors": 4,
                        "power": "167 bhp @ 3,750 rpm",
                        "boot_space": "425 liters",
                        "seating_capacity": 5,
                        "max_torque": "350 Nm @ 1,750-2,500 rpm"
                    },
                    {
                        "model": "Tigor",
                        "mileage": "20.3 kmpl",
                        "doors": 4,
                        "power": "84 bhp @ 6,000 rpm",
                        "boot_space": "419 liters",
                        "seating_capacity": 5,
                        "max_torque": "113 Nm @ 3,300 rpm"
                    },
                    {
                        "model": "Altroz",
                        "mileage": "25.11 kmpl",
                        "doors": 4,
                        "power": "84 bhp @ 6,000 rpm",
                        "boot_space": "345 liters",
                        "seating_capacity": 5,
                        "max_torque": "113 Nm @ 3,300 rpm"
                    },
                    {
                        "model": "Safari",
                        "mileage": "16.14 kmpl",
                        "doors": 4,
                        "power": "168 bhp @ 3,750 rpm",
                        "boot_space": "447 liters",
                        "seating_capacity": 7,
                        "max_torque": "350 Nm @ 1,750-2,500 rpm"
                    }
                ]
            },
            {
                "brand": "Toyota",
                "models": [
                    {
                        "model": "Innova Crysta",
                        "mileage": "13.68 kmpl",
                        "doors": 5,
                        "power": "148 bhp @ 3,400 rpm",
                        "boot_space": "300 liters",
                        "seating_capacity": 7,
                        "max_torque": "343 Nm @ 1,400-2,800 rpm"
                    },
                    {
                        "model": "Fortuner",
                        "mileage": "15.04 kmpl",
                        "doors": 5,
                        "power": "201 bhp @ 3,400 rpm",
                        "boot_space": "296 liters",
                        "seating_capacity": 7,
                        "max_torque": "500 Nm @ 1,600-2,400 rpm"
                    },
                    {
                        "model": "Corolla Altis",
                        "mileage": "21.43 kmpl",
                        "doors": 4,
                        "power": "138 bhp @ 6,400 rpm",
                        "boot_space": "470 liters",
                        "seating_capacity": 5,
                        "max_torque": "173 Nm @ 4,000 rpm"
                    },
                    {
                        "model": "Yaris",
                        "mileage": "17.1 kmpl",
                        "doors": 4,
                        "power": "105 bhp @ 6,000 rpm",
                        "boot_space": "476 liters",
                        "seating_capacity": 5,
                        "max_torque": "140 Nm @ 4,200 rpm"
                    },
                    {
                        "model": "Camry",
                        "mileage": "19.16 kmpl",
                        "doors": 4,
                        "power": "176 bhp @ 6,000 rpm",
                        "boot_space": "420 liters",
                        "seating_capacity": 5,
                        "max_torque": "221 Nm @ 3,600-5,200 rpm"
                    },
                    {
                        "model": "Etios",
                        "mileage": "16.78 kmpl",
                        "doors": 4,
                        "power": "67 bhp @ 5,500 rpm",
                        "boot_space": "592 liters",
                        "seating_capacity": 5,
                        "max_torque": "170 Nm @ 1,800-2,400 rpm"
                    }
                ]
            },
            {
                "brand": "Kia",
                "models": [
                    {
                        "model": "Seltos",
                        "mileage": "16.8 kmpl",
                        "doors": 5,
                        "power": "115 bhp @ 6,300 rpm",
                        "boot_space": "433 liters",
                        "seating_capacity": 5,
                        "max_torque": "144 Nm @ 4,500 rpm"
                    },
                    {
                        "model": "Sonet",
                        "mileage": "24.1 kmpl",
                        "doors": 5,
                        "power": "118 bhp @ 6,000 rpm",
                        "boot_space": "392 liters",
                        "seating_capacity": 5,
                        "max_torque": "172 Nm @ 1,500-4,000 rpm"
                    },
                    {
                        "model": "Carnival",
                        "mileage": "13.9 kmpl",
                        "doors": 5,
                        "power": "197 bhp @ 3,800 rpm",
                        "boot_space": "540 liters",
                        "seating_capacity": 9,
                        "max_torque": "440 Nm @ 1,750-2,750 rpm"
                    },
                    {
                        "model": "Rio",
                        "mileage": "18.0 kmpl",
                        "doors": 5,
                        "power": "85 bhp @ 3,750 rpm",
                        "boot_space": "450 liters",
                        "seating_capacity": 5,
                        "max_torque": "215 Nm @ 1,500-3,750 rpm"
                    },
                    {
                        "model": "Stinger",
                        "mileage": "12.6 kmpl",
                        "doors": 4,
                        "power": "365 bhp @ 6,000 rpm",
                        "boot_space": "406 liters",
                        "seating_capacity": 5,
                        "max_torque": "510 Nm @ 1,300-4,500 rpm"
                    },
                    {
                        "model": "Picanto",
                        "mileage": "23.0 kmpl",
                        "doors": 5,
                        "power": "76 bhp @ 6,000 rpm",
                        "boot_space": "255 liters",
                        "seating_capacity": 5,
                        "max_torque": "96 Nm @ 4,000 rpm"
                    }
                ]
            }
        ]
        for brand_entry in data:
            brand_name = brand_entry["brand"]
            models_data = brand_entry["models"]

            # Create or get the Carbrand object
            carbrand, created = Carbrand.objects.get_or_create(
                carbrand=brand_name)

            # Iterate through the models and insert data
            for model_entry in models_data:
                Carmodel.objects.create(
                    carbrand=carbrand,
                    carmodel=model_entry["model"],
                    mileage=model_entry["mileage"],
                    doors=model_entry["doors"],
                    power=model_entry["power"],
                    boot_space=model_entry["boot_space"],
                    seating_capacity=model_entry["seating_capacity"],
                    max_torque=model_entry["max_torque"]
                )

                self.stdout.write(self.style.SUCCESS(
                    f'Successfully inserted data for {brand_name} - {model_entry["model"]}'))
