from config import client, MODEL


def main():
    print("\n=== STRUCTURED OUTPUT DEMO ===\n")

    # 1. Free text
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Give one short tip for learning AI."}
        ],
    )
    print("FREE TEXT:")
    print(response.choices[0].message.content)

    # 2. JSON object
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    "Return a JSON object with keys "
                    "name and field for a fictional AI student."
                ),
            }
        ],
        response_format={"type": "json_object"},
    )
    print("\nJSON OBJECT:")
    print(response.choices[0].message.content)

    # 3. Strict JSON schema
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "field": {"type": "string"},
            "year": {"type": "integer"},
        },
        "required": ["name", "field", "year"],
        "additionalProperties": False,
    }

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    "Return a fictional AI student with name, field, "
                    "and year."
                ),
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "student_profile",
                "strict": True,
                "schema": schema,
            },
        },
    )

    print("\nSTRICT JSON SCHEMA:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()