from app.domain.issue import Issue


class RuffParser:
    @staticmethod
    def parse(data: list[dict]) -> list[Issue]:
        issues: list[Issue] = []

        for item in data:
            issues.append(
                Issue(
                    code=item["code"],
                    message=item["message"],
                    severity=item["severity"],
                    line=item["location"]["row"],
                    column=item["location"]["column"],
                    source="ruff",
                )
            )

        return issues