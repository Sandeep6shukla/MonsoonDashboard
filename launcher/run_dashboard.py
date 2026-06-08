import subprocess


commands = [

    "uv run python main.py",

    "uv run python -m collectors.urban.mumbai.mcgm",

    "uv run python -m processes.urban.mumbai.process_mcgm",

    "uv run python -m dashboard.generate_dashboard"

]


for command in commands:

    print()
    print("=" * 60)
    print(command)
    print("=" * 60)

    subprocess.run(
        command,
        shell=True,
        check=True
    )

print()
print("=" * 60)
print("DASHBOARD READY")
print("=" * 60)