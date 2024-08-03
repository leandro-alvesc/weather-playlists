from firedantic import Model, ModelNotFoundError
from typing import Self


class FirestoreBaseModel(Model):
    @classmethod
    def find_one_or_none(cls, filter: dict) -> Self:
        try:
            obj = cls.find_one(filter_=filter)
            return obj
        except ModelNotFoundError:
            return None

    @classmethod
    def get_by_id(cls, id_: str) -> Self:
        try:
            return super().get_by_id(id_)
        except ModelNotFoundError:
            return None
