from typing import Dict
import uuid

class TripCreator:
    def __init__(self, trips_repository, emails_repository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())

            # **body... = quando tiramos todos os elementos de um dicionário e colocamos em outro
            trips_infos = { **body, "id": trip_id }

            self.__trips_repository.create_trip(trips_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
            return {
                "body": { "id": trip_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }
