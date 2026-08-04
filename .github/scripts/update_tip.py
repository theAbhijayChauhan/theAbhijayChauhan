"""
Daily DevOps Tip updater for GitHub Profile README.
Fetches a fresh tech/dev tip from a free API and injects it
between the <!-- TECH-TIP-START --> and <!-- TECH-TIP-END --> markers.
"""

import re
import random
import requests
from datetime import datetime, timezone

# ── Curated DevOps tips pool (used as fallback + supplemented by API) ──────────
DEVOPS_TIPS = [
    "Always version-control your Terraform state configurations. Use remote backends like AWS S3 + DynamoDB for state locking — it prevents race conditions in team environments.",
    "Use multi-stage Docker builds to keep your final images lean. Only copy the compiled artifact, not the full build toolchain — slashes image size by 60–80%.",
    "In Kubernetes, set resource `requests` and `limits` for every container. Without them, a single runaway pod can starve the entire node and cause cascading failures.",
    "GitHub Actions secrets are encrypted at rest. Never echo them in logs — even `echo $SECRET` in CI can leak partial values through log formatting bugs.",
    "Always pin your Docker base images to a specific digest (`sha256:...`), not just a tag. Tags are mutable; digests are immutable — critical for reproducible builds.",
    "Use `kubectl rollout undo` to instantly revert a bad deployment. Pair it with `--to-revision=N` to jump back to any specific historical version.",
    "Jenkins pipelines should be written as `Jenkinsfile` in your repo — not configured through the UI. This makes your CI/CD infrastructure as code, fully reviewable and versioned.",
    "In Terraform, always run `terraform plan` and review the diff before `terraform apply`. Automation without review in production IaC is a recipe for disaster.",
    "AWS IAM: Apply the principle of least privilege. Never use the root account for daily tasks — create IAM roles with scoped permissions and rotate access keys regularly.",
    "Use `docker compose` for local dev environments that mirror production. Define services, networks, and volumes declaratively so the entire stack spins up with one command.",
    "GCP Cloud Run auto-scales to zero when idle — perfect for infrequent workloads. You only pay for actual request processing time, not idle compute.",
    "Set up `pre-commit` hooks in your repos to auto-lint, format, and run security scans before every commit. Catch issues locally before they ever hit CI.",
    "Use Kubernetes `readinessProbe` and `livenessProbe` for all production pods. Without them, traffic gets routed to pods that aren't ready, causing cascading 502 errors.",
    "Terraform modules are your best friend for DRY infrastructure. Extract repeated patterns (VPCs, EKS clusters) into reusable modules with clean variable interfaces.",
    "In GitHub Actions, use `concurrency` groups to cancel in-progress workflow runs when a new commit is pushed. Prevents queued pipelines from piling up on every push.",
    "Python virtual environments (`venv`) should always be excluded from Docker images. Use multi-stage builds and install directly into the final image layer.",
    "Monitor your Kubernetes cluster with resource quotas at the namespace level. It prevents any single team or app from consuming all cluster resources.",
    "Use `bash -euo pipefail` at the top of every shell script in CI. `-e` exits on error, `-u` errors on unset vars, `-o pipefail` catches failures in piped commands.",
    "Blue-green deployments eliminate downtime: run two identical environments, switch traffic instantly between them, and keep the old one as an instant rollback.",
    "Always use `.dockerignore` in your Docker builds. Excluding `node_modules`, `.git`, and test files can reduce build context size by 90% and dramatically speed up builds.",
    "Canary releases let you test new code on 5-10% of real traffic before full rollout. Use Kubernetes traffic splitting or AWS weighted routing to implement this safely.",
    "Tag every cloud resource with `env`, `team`, `project`, and `cost-center` labels. Without tagging, cloud cost attribution becomes impossible to debug at scale.",
    "Use `helm diff` plugin before every `helm upgrade`. It shows exactly what will change in your cluster — treat it like `terraform plan` for Kubernetes.",
    "Log aggregation is non-negotiable in production. Tools like ELK Stack, Loki + Grafana, or AWS CloudWatch Logs let you search across all services from one place.",
    "Use GitHub branch protection rules: require PR reviews, passing CI checks, and signed commits before merging to `main`. Never push directly to production branches.",
]

README_PATH = "README.md"
START_MARKER = "<!-- TECH-TIP-START -->"
END_MARKER = "<!-- TECH-TIP-END -->"


def fetch_api_quote() -> str | None:
    """Try to fetch a fresh quote from ZenQuotes API."""
    try:
        resp = requests.get(
            "https://zenquotes.io/api/random",
            timeout=8,
            headers={"User-Agent": "GitHub-Profile-Updater/1.0"},
        )
        if resp.status_code == 200:
            data = resp.json()
            if data and isinstance(data, list):
                q = data[0]
                return f'"{q["q"]}" — *{q["a"]}*'
    except Exception:
        pass
    return None


def get_tip() -> str:
    """Return today's tip: API quote wrapped with a DevOps tip, or fallback."""
    today_idx = datetime.now(timezone.utc).timetuple().tm_yday  # 1–365
    tip = DEVOPS_TIPS[today_idx % len(DEVOPS_TIPS)]
    api_quote = fetch_api_quote()

    date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")

    if api_quote:
        return (
            f"> 💡 **Daily DevOps Tip** `{date_str}`\n"
            f">\n"
            f"> {tip}\n"
            f">\n"
            f"> 📖 *Quote of the day:* {api_quote}"
        )
    else:
        return (
            f"> 💡 **Daily DevOps Tip** `{date_str}`\n"
            f">\n"
            f"> {tip}"
        )


def update_readme(tip: str) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    replacement = f"{START_MARKER}\n{tip}\n{END_MARKER}"

    if not pattern.search(content):
        print("❌ Markers not found in README.md — aborting.")
        return

    new_content = pattern.sub(replacement, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[OK] README updated successfully for {datetime.now(timezone.utc).strftime('%Y-%m-%d')}!")
    print(f"\n[TIP] Tip injected:\n{tip.encode('ascii', errors='replace').decode()}")


if __name__ == "__main__":
    tip = get_tip()
    update_readme(tip)
