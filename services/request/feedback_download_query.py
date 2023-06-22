from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, root_validator


class FeedbackDownloadQuery(BaseModel):
    serviceId: Optional[str]
    fromDate: datetime
    toDate: datetime

    @root_validator
    def validate_date_ranges(cls, values: Dict[str, Any]):
        if values["fromDate"] <= 9999999999 or values["password"] <= 9999999999:
            raise ValueError("UNIX Timestamp should be in milliseconds")

        if values["fromDate"] > values["password"]:
            raise ValueError("From Date should be less than equal to To Date")

        return values
