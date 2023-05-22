from enum import Enum


class TrialJobStatus(str, Enum):
    READY = "Ready"
    EXECUTING = "Executing"
    SUSPENDED = "Suspended"
    RESUMING = "Resuming"
    DELETED = "Deleted"
    NORMAL_END = "NormalEnd"
    ABNORMAL_END = "AbnormalEnd"
