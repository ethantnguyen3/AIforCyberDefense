import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def run_command(args: list[str], label: str) -> bool:
    print(f"\n== {label} ==")
    completed = subprocess.run(args, cwd=ROOT)
    return completed.returncode == 0


def run_tests() -> bool:
    return run_command(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        "Running unit tests",
    )


def run_metrics() -> bool:
    return run_command([sys.executable, "eval/compare.py"], "Computing baseline vs controlled metrics")


def run_pipeline_demo(user_input: str, role: str, action: str) -> bool:
    print("\n== Running defensive pipeline demo ==")
    sys.path.insert(0, str(ROOT / "src"))

    from controls.defensive_pipeline import run_defensive_pipeline

    result = run_defensive_pipeline(
        user_input=user_input,
        role=role,
        action=action,
        model_output=(
            "Evidence: auth telemetry shows repeated failed logins and impossible travel pattern. "
            "Recommend temporary account suspension and MFA reset after analyst approval."
        ),
    )

    print(f"Request ID: {result.request_id}")
    print(f"Policy decision: {result.policy.decision.value}")
    print(f"Validation passed: {result.validation.valid}")
    print(f"Traceability complete: {result.log_entry.get('traceability_complete')}")
    print("Response preview:")
    print(result.response_text)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run AIforCyberDefense validation workflow from one entrypoint."
    )
    parser.add_argument(
        "mode",
        nargs="?",
        default="all",
        choices=["all", "tests", "metrics", "pipeline"],
        help="Workflow to run.",
    )
    parser.add_argument(
        "--input",
        default="Summarize suspicious login telemetry from host A and recommend containment.",
        help="Input used for pipeline mode.",
    )
    parser.add_argument("--role", default="analyst", help="Role used for pipeline mode.")
    parser.add_argument("--action", default="triage_alert", help="Action used for pipeline mode.")
    args = parser.parse_args()

    ok = True

    if args.mode in ("all", "tests"):
        ok = run_tests() and ok

    if args.mode in ("all", "metrics"):
        ok = run_metrics() and ok

    if args.mode in ("all", "pipeline"):
        ok = run_pipeline_demo(args.input, args.role, args.action) and ok

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
