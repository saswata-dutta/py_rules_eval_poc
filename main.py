from pprint import pprint
from dataclasses import dataclass
from engine import getBestOutcome
from rules import getB2bRules
from rules import getB2bThresholds
from rules import getB2bSchedule


@dataclass(frozen=True)
class Account:
    id: str
    netAr: int
    riskBin: str

def process(account, rules, thresholds):
    outcome = getBestOutcome(rules, account, thresholds)
    schedule = getB2bSchedule(outcome)

    return {'outcome' : outcome, 'schedule' : schedule}

def handle(accounts):
    rules = getB2bRules()
    thresholds = getB2bThresholds()

    return { account.id : process(account, rules, thresholds) for account in accounts }


########

def main():
    accounts = [
    Account("001", 10000, "BIN_3"),
    Account("002", 10000, "BIN_2"),
    Account("003", 10000, "BIN_1"),
    Account("004", -10, None)
    ]

    pprint(handle(accounts))

########

if __name__ == "__main__":
    main()
