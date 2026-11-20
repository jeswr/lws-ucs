#!/usr/bin/env python3
"""Rework the LWS requirement clean-up PRs (w3c/lws-ucs #233-#265) to keep every
requirement and give it a status, instead of deleting requirements.

What it does:
  1. Pushes 34 branches from requirement-branches.bundle to your fork
     (fast-forward only: one new commit on each existing PR branch, plus the new
     branch req/status-definitions).
  2. Updates each PR's title and body: adds the status, swaps "Closes #N" for
     "Refs #N" so no use case issue closes on merge, and retitles the 19 former
     delete PRs as "mark not addressed / afforded / supported".
  3. Swaps the requirement-delete label for requirement-modify on those 19 PRs.
  4. Opens the new PR that defines the three statuses.

It does not merge, close or comment on anything. It is safe to run again.

Usage (from the folder holding this script, plan.json and the bundle):
  python3 redirect-requirement-prs.py --dry-run
  python3 redirect-requirement-prs.py
Needs git, Python 3 and the GitHub CLI logged in as you (gh auth status).
If git can't push over HTTPS, run `gh auth setup-git` once, or pass
--remote git@github.com:jeswr/lws-ucs.git
"""
import argparse, json, os, re, subprocess, sys, tempfile

UP = "w3c/lws-ucs"
HERE = os.path.dirname(os.path.abspath(__file__))
STRUCT_BRANCH = "req/status-definitions"
STRUCT_TITLE = "[Class 3] Define requirement statuses: supported, afforded, not addressed by LWS 1.0"
STRUCT_BODY = """<!-- claude-projects-attribution: {"github_login":"jeswr"} -->
_Requested by **Jesse** · [project thread](https://claude.ai/code/project/chan_01QLamxq2PNXaJAsaRNKfZKE?thread=cmsg_01QLamxq2PNXaJAsaRNKfZKE8dgqEnziLCFDddbj6nAGb9)_

Replaces the sentence above the requirements list with definitions of three statuses, which each requirement now states against the LWS 1.0 specifications:

- **Supported**: the specifications define a mechanism that meets the requirement.
- **Afforded**: the specifications are designed so that implementations can meet it, but do not specify how.
- **Not addressed by LWS 1.0**: no LWS 1.0 specification defines or accommodates it. It stays in the document, with its use cases, to inform future work.

This follows the discussion on public-lws-wg (Christoph Braun, 5 and 9 November) and at the 9 November WG meeting: requirements the specifications don't meet stay in the published document instead of being deleted. Requirements keep the WG's priority order, and each gets a stable identifier. The requirement PRs (#233 to #265) each add the status line for their own requirement.

**Process (Class 3):** merged by lazy consensus after one week unless someone objects.
**Earliest merge:** 19 November 2026.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01KLrUetwgGPc6hXWdNXDGJj
"""


def run(cmd, dry=False, check=True, cwd=None, capture=True):
    if dry:
        print("    would run:", " ".join(cmd))
        return ""
    r = subprocess.run(cmd, cwd=cwd, text=True, capture_output=capture)
    if check and r.returncode != 0:
        raise SystemExit(f"Command failed: {' '.join(cmd)}\n{r.stderr}")
    return r.stdout


def new_body(body, entry):
    if "**Status:**" in body:
        return None  # already updated
    body = re.sub(r"\bCloses #(\d+)", r"Refs #\1", body)
    for old, new in entry.get("replace", []):
        body = body.replace(old, new)
    first, sep, rest = body.partition("\n\n")
    status = "**Status:** " + entry["status"]
    if entry["kind"] == "status":
        return entry["summary"] + "\n\n" + status + sep + rest
    return first + "\n\n" + status + "\n\n" + entry["note"] + sep + rest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--remote", default="https://github.com/jeswr/lws-ucs.git")
    ap.add_argument("--fork-owner", default="jeswr")
    ap.add_argument("--skip-push", action="store_true", help="branches are already on the fork")
    a = ap.parse_args()
    dry = a.dry_run
    plan = {int(k): v for k, v in json.load(open(os.path.join(HERE, "plan.json"))).items()}

    if a.skip_push:
        print("1. Skipping branch push (--skip-push)")
    else:
        push_branches(a, dry)
    update_prs(a, dry, plan)


def push_branches(a, dry):
    bundle = os.path.join(HERE, "requirement-branches.bundle")
    print("1. Pushing branches to", a.remote)
    tmp = tempfile.mkdtemp()
    run(["git", "init", "-q", tmp])
    run(["git", "fetch", "-q", bundle, "refs/heads/req/*:refs/heads/req/*"], cwd=tmp)
    branches = run(["git", "for-each-ref", "--format=%(refname:short)", "refs/heads/req/"], cwd=tmp).split()
    failed = []
    for b in branches:
        if dry:
            print(f"    would push {b}")
            continue
        r = subprocess.run(["git", "push", "-q", a.remote, f"{b}:{b}"], cwd=tmp, text=True, capture_output=True)
        if r.returncode != 0 and "up-to-date" not in r.stderr:
            failed.append(b)
            print(f"    FAILED {b}: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ''}")
        else:
            print(f"    pushed {b}")
    if failed:
        print("\nSome branches did not push (probably changed on the fork since the bundle was made). "
              "Nothing else was changed. Tell Claude which ones and it will rebuild them.")
        sys.exit(1)



def update_prs(a, dry, plan):
    print("\n2. Updating PR titles, bodies and labels on", UP)
    for n in sorted(plan):
        e = plan[n]
        pr = json.loads(run(["gh", "pr", "view", str(n), "--repo", UP, "--json", "title,body,headRefName,state"]))
        if pr["headRefName"] != e["branch"]:
            print(f"    #{n}: head is {pr['headRefName']}, expected {e['branch']}; skipped")
            continue
        if pr["state"] != "OPEN":
            print(f"    #{n}: {pr['state'].lower()}; skipped")
            continue
        body = new_body(pr["body"], e)
        args = []
        if pr["title"] != e["title"]:
            args += ["--title", e["title"]]
        if body is not None:
            args += ["--body", body]
        if e["kind"] == "status":
            args += ["--remove-label", "requirement-delete", "--add-label", "requirement-modify"]
        if not args:
            print(f"    #{n}: already up to date")
            continue
        print(f"    #{n}: {e['title']}")
        run(["gh", "pr", "edit", str(n), "--repo", UP] + args, dry=dry)

    print("\n3. Opening the status definitions PR")
    existing = json.loads(run(["gh", "pr", "list", "--repo", UP, "--head", STRUCT_BRANCH, "--state", "all", "--json", "number,state"]))
    if existing:
        print(f"    already exists: #{existing[0]['number']} ({existing[0]['state'].lower()})")
    else:
        run(["gh", "pr", "create", "--repo", UP, "--base", "main", "--head", f"{a.fork_owner}:{STRUCT_BRANCH}",
             "--title", STRUCT_TITLE, "--body", STRUCT_BODY, "--label", "class-3"], dry=dry, capture=False)
    print("\nDone." if not dry else "\nDry run only: nothing was changed.")


if __name__ == "__main__":
    main()
