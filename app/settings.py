from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    mongo_user: str
    mongo_password: str
    mongo_host: str = "clouster.mnoc96q.mongodb.net"
    mongo_db: str = "supertmarket"
    mongo_protocol: str = "mongodb+srv"
    mongo_options: str = "?retryWrites=true&w=majority&appName=Clouster"

    # <-- Aquí configuramos el .env:
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def mongo_url(self) -> str:
        options = self.mongo_options if self.mongo_options else ""
        if options and not options.startswith("?"):
            options = f"?{options}"
        return f"{self.mongo_protocol}://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}/{options}"

# Al instanciar, BaseSettings leerá las vars del .env
settings = AppSettings()
