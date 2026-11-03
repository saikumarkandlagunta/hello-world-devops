# Hello World DevOps Lab

A tiny, familiar web app for learning GitHub and AWS DevOps work. It serves `Hello, world!` at `/` and returns a simple health response from `/health`.

We will use this same app as the workload while learning source control, Linux and networking, EC2, containers, ECR, ECS, deployments, and monitoring. The first version runs locally and listens only on your computer.

## What you need

- Python 3.10 or newer
- PowerShell
- Git
- GitHub CLI (`gh`) for the GitHub command exercises

## Run it manually in PowerShell

Open PowerShell in this project folder and check Python:

```powershell
python --version
```

Create and activate a virtual environment. This keeps the project's Python packages separate from other projects:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Otherwise, install the dependency and start the app:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Keep that terminal open. The server listens only on your computer at `http://127.0.0.1:5000`.

## Try the app from a second PowerShell window

Open the home page:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/
```

Check health:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/health
```

Stop the server with `Ctrl+C` in the terminal where it is running.

## Git and GitHub practice

Follow [GITHUB_DAY_TO_DAY.md](GITHUB_DAY_TO_DAY.md) for the hands-on command guide, including local Git, GitHub CLI, branches, issues, pull requests, and safe recovery.

## What to notice

- `/` is the familiar Hello World page.
- `/health` returns a small JSON response suitable for a basic health check.
- The server prints request information in its terminal; those messages are the first logs you can inspect.
- The server binds to `127.0.0.1`, so it is not exposed to your network.
