class DiscourseError(Exception):
    pass


class RateLimitError(DiscourseError):
    pass


class UnauthorizedError(DiscourseError):
    pass


class PageNotFoundError(DiscourseError):
    pass
