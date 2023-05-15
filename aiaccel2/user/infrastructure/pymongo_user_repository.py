from typing import Dict, List, Optional

import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient

from aiaccel2.user.domain.user import User
from aiaccel2.user.domain.user_repository import UserRepository


class PyMongoUserRepository(UserRepository):

    def __init__(self) -> None:
        client: MongoClient = pymongo.MongoClient(
            "mongodb://mongo:27017/user")
        self.database = client.user

    def find_all(self) -> List[User]:
        users = self.database.user.find()
        return [self._create_user(user) for user in users]

    def find(self, user_id: str) -> Optional[User]:
        user = self.database.user.find_one({"_id": ObjectId(user_id)})
        return None if not user else self._create_user(user)

    def save(self, user: User) -> None:
        self.database.user.insert_one({
            "_id": ObjectId(user.user_id),
            "name": user.name,
            "email": user.email
        })

    def delete(self, user_id: str) -> None:
        self.database.user.delete_one({"_id": ObjectId(user_id)})

    def update(self, user: User) -> Optional[User]:
        record = self.database.user.update_one(
            {"_id": ObjectId(user.user_id)}, {
                '$set': {
                    'email': user.email,
                    'name': user.name,
                }
            },
            upsert=False)
        return None if not record else self.find(user.user_id)

    @staticmethod
    def _create_user(user: Dict) -> User:
        return User(user_id=str(ObjectId(user["_id"])), name=user["name"], email=user["email"])
