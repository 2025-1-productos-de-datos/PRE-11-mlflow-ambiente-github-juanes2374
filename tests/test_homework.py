import os
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")

def test_01():
    try:
        if sys.platform == "win32":
            # Windows: ejecuta run.bat
            subprocess.run(["cmd", "/c", "run.bat"], check=True)
        else:
            # Linux/Mac: ejecuta run.sh
            subprocess.run(["bash", "run.sh"], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    assert os.path.exists("mlruns"), "mlruns directory does not exist."
    experiments = [
        d for d in os.listdir("mlruns") if os.path.isdir(os.path.join("mlruns", d))
    ]
    assert len(experiments) > 0, "No experiments found in mlruns directory."
