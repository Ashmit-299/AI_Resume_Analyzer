from dataclasses import dataclass, field


@dataclass
class JobDescription:
    title: str | None = None
    skills: list[str] = field(default_factory=list)
    raw_text: str = ""