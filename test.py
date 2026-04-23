import os
import sys


def main() -> None:
    print("Starting intentional failure script...")

    github_actions = os.getenv("GITHUB_ACTIONS", "false").lower() == "true"

    if github_actions:
        print("Running inside GitHub Actions.")
        raise RuntimeError("Intentional failure triggered inside GitHub Actions for testing.")

    print("Not running inside GitHub Actions. Exiting successfully.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


...
