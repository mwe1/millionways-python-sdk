# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GetUserListResponse"]


class GetUserListResponse(BaseModel):
    users: Optional[List[str]] = None
