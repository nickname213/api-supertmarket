from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    mongo_user: str
    mongo_password: str
    mongo_host: str = "clouster.mnoc96q.mongodb.net"
    mongo_db: str = "supertmarket"
    mongo_protocol: str = "mongodb+srv"
    mongo_options: str = "?retryWrites=true&w=majority&appName=Clouster"

    @property
    def mongo_url(self) -> str:
        options = self.mongo_options if self.mongo_options else ""
        if options and not options.startswith("?"):
            options = f"?{options}"
        return f"{self.mongo_protocol}://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}/{options}"

settings = AppSettings()
