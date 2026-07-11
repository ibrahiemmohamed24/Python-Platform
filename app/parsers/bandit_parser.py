from app.domain.issue import Issue


class BanditParser:
    @staticmethod
    def parse(data: list[dict]) -> list[Issue]:
        issues: list[Issue] = []

        for item in data:
            issues.append(
                Issue(
                    code=item["test_id"],
                    message=item["issue_text"],
                    severity=item["issue_severity"].lower(),
                    line=item["line_number"],
                    column=0,
                    source="bandit",
                )
            )

        return issues