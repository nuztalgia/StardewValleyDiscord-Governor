from config import ADMIN_ACCESS
from commonbot.utils import checkRoles

"""
Requires admin

Wrapper function for commands that has them do nothing if the author doesn't have the admin role
"""
def requires_admin(func):
    async def wrapper(*args, **kwargs):
        # expect message to be the last argument
        message = args[-1]

        if checkRoles(message.author, ADMIN_ACCESS):
            return await func(*args, **kwargs)
        else:
            return None

    return wrapper
