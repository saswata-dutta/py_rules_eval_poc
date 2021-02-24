GLOBALS = {'__builtins__': None}

def getOutcome(rule, account, thresholds):
    return eval(rule.expr, GLOBALS, {'account': account, 'thresholds': thresholds})

def getBestOutcome(rules, account, thresholds):
    passed = next(filter(lambda rule : getOutcome(rule, account, thresholds), rules))
    assert passed, "No rule fired for {account} with {thresholds}"
    return passed.outcome
