from models.user import User
from persistence.IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.users = []  # Data storage list for users

    def save(self, entity):
        # Save a user entity
        if isinstance(entity, User):
            # Generate user ID (Assuming email as the unique identifier)
            user_id = len(self.users) + 1
            entity.id = user_id
            self.users.append(entity)
            return {'id': user_id}  # Return the ID of the newly created user
        else:
            raise TypeError("Entity must be an instance of User.")

    def get(self, entity_id, entity_type):
        # Get a user by ID
        if entity_type == 'user':
            for user in self.users:
                if user.id == entity_id:
                    return user
        return None

    def update(self, entity):
        # Update a user entity
        if isinstance(entity, User):
            user_id = entity.id
            for idx, user in enumerate(self.users):
                if user.id == user_id:
                    self.users[idx] = entity
                    return True
        return False

    def delete(self, entity_id, entity_type):
        # Delete a user by ID
        if entity_type == 'user':
            for user in self.users:
                if user.id == entity_id:
                    self.users.remove(user)
                    return True
        return False
