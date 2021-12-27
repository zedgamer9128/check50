from ._api import run, log, Failure
import subprocess

# check if Rust is installed.
# if not, raise an error.
# if it is, continue.
ver = run("rustc --version").stdout()
if not ver.startswith("rustc"):
    log("Rust is not installed.")
    raise Failure("Rust is not installed.")
cargo = run("cargo --version").stdout()
if not cargo.startswith("cargo"):
    log("Cargo is not installed.")
    raise Failure("Cargo is not installed.")

def compile(file):
    """
    Check if the Rust code compiles.
    """
    # If there are args
    if file:
        # If there are args, run the command with args.
        # If the command fails, raise an error.
        # If the command succeeds, continue.
        log("Compiling the Rust code...")
        check = run(f"rustc {file}")
    else:
        log("Compiling the Rust code...")
        check = subprocess.run(["cargo", "build"], capture_output=True)
    if check.returncode != 0:
        log("Rust code did not compile.")
        raise Failure("Rust code did not compile.")
    log("Rust code compiled.")
