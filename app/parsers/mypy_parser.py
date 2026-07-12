import json

from app.domain.issue import Issue


class MypyParser:
    @staticmethod
    def parse(stdout: str) -> list[Issue]:
        issues: list[Issue] = []

        for line in stdout.splitlines():
            if not line.strip():
                continue

            item = json.loads(line)

            issues.append(
                Issue(
                    code=item["code"],
                    message=item["message"],
                    severity=item["severity"],
                    line=item["line"],
                    column=item["column"],
                    source="mypy",
                )
            )

        return issues