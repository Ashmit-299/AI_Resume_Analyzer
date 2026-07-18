from dataclasses import dataclass, field


@dataclass
class Resume:
    name: str | None = None
    email: str |None = None
    phone: str | None = None

    github: str | None = None
    linkedin: str | None = None

    skills: list[str] = field(default_factory=list)
    education: list[str] = field(default_factory=list)
    experience: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)

    raw_text: str = ""