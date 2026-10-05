from robust_agent import handle_tool_call


class FakeFunction:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class FakeCall:
    def __init__(self, name, arguments):
        self.function = FakeFunction(name, arguments)
        self.id = "fault-test"


CASES = [
    ("malformed JSON", FakeCall("calculator", '{"expression": 2 + }')),
    ("unknown tool", FakeCall("does_not_exist", '{"x": 1}')),
    ("missing argument", FakeCall("get_course_fee", '{}')),
    ("wrong type", FakeCall("get_course_fee", '{"course_code": 123}')),
    ("invalid enum", FakeCall("get_course_fee", '{"course_code": "CS101", "semester": "summer"}')),
    ("extra argument", FakeCall("get_course_fee", '{"course_code": "CS101", "year": 2026}')),
    ("empty arguments", FakeCall("calculator", '')),
    ("wrong JSON type", FakeCall("calculator", '["2 + 2"]')),
    ("wrong tool capitalization", FakeCall("GET_COURSE_FEE", '{"course_code": "CS101"}')),
    ("arguments is JSON array", FakeCall("calculator", '["2 + 2"]')),
]


for name, call in CASES:
    try:
        result = handle_tool_call(call)
        print(f"{name:30} -> {result}")
    except Exception as exc:
        print(f"{name:30} -> EXCEPTION: {exc}")