from dataclasses import dataclass
from typing import Final, Any

@dataclass(frozen=True)
class Rule:
    expr: Any
    outcome: str
    # todo -> namespace, name, priority if stored in a db


@dataclass(frozen=True)
class Thresholds:
    ArLow: int
    ArHigh: int


B2B_RULE_DEFS: Final = [
    ("account.netAr < thresholds.ArLow", "FULLY_AUTOMATED"),
    ("account.netAr > thresholds.ArHigh and account.riskBin == 'BIN_3'", "FULLY_AUTOMATED"),
    ("account.netAr > thresholds.ArHigh and account.riskBin == 'BIN_2'", "HIGH_TOUCH"),
    ("account.netAr > thresholds.ArHigh and account.riskBin == 'BIN_1'", "LOW_TOUCH")
]


B2B_SCHEDULES: Final = {
    "FULLY_AUTOMATED" : [(1, "EMAIL", "TEMPLATE_1"), (15, "EMAIL", "TEMPLATE_2"), (20, "EMAIL", "TEMPLATE_3")],
    "HIGH_TOUCH" : [(1, "EMAIL", "TEMPLATE_3"), (15, "CALL"), (20, "CALL")],
    "LOW_TOUCH" : [(1, "EMAIL", "TEMPLATE_1"), (15, "EMAIL", "TEMPLATE_2"), (20, "EMAIL", "TEMPLATE_3"), (30, "CALL")]
}


def getB2bRules():
    return [Rule(compile(expr, "<string>", "eval"), outcome) for expr, outcome in B2B_RULE_DEFS]


def getB2bThresholds():
    return Thresholds(0, 10)


def getB2bSchedule(outcome):
    return B2B_SCHEDULES[outcome]
