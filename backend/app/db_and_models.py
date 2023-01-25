from typing import Optional

from sqlmodel import Field, SQLModel


class YouTubeContent(SQLModel):
    image_url: str
    title: str
    description: str
    link: str


class YouTube(YouTubeContent, table=True):
    __tablename__ = "youtube"

    id: Optional[int] = Field(default=None, primary_key=True)
