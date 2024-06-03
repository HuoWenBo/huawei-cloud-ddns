from typing import Literal, Type, Tuple

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict, JsonConfigSettingsSource, PydanticBaseSettingsSource


class Result(BaseModel):
    type: Literal["json", "text"] = "text"
    key: str | int = None


class Settings(BaseSettings):
    cloud_sdk_ak: str
    cloud_sdk_sk: str
    zone_id: str
    recordset_id: str
    name: str
    rate: int
    url_pool: dict[str, Result]

    model_config = SettingsConfigDict(
        json_file="config.json",
        json_file_encoding="utf-8"
    )

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: Type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return JsonConfigSettingsSource(settings_cls),


settings = Settings()
