from pydantic import BaseSettings


# Any of these can be overridden via environment variables with matching names
class Settings(BaseSettings):
    # User or organization name, used for "user/image" -name generation
    DOCKER_USER = "fbjorn"

    # List of images that should be built beforehand
    PRIORITY_BUILDS = []


conf = Settings()
