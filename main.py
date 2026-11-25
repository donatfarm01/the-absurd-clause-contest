"""The Absurd Clause Contest - entry program.

Writes one absurd terms-of-service clause to /output/entry.txt. The
clause opens like a genuine account-succession provision - the kind of
deadpan boilerplate a reader skims past - and then the absurdity
ambushes: on the user's death the account passes to their eldest
houseplant, subject to a ninety-day probationary period. One clean
sentence, 130 characters, no wasted words.
"""

ENTRY = "In the event the user dies, their account shall pass to their eldest houseplant, subject to a ninety (90) day probationary period."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
