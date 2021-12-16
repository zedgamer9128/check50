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

def compile():
    """
    Check if the Rust code compiles.
    """
    log("Compiling the Rust code...")
    check = subprocess.run(["cargo", "build"], capture_output=True)
    if check.returncode != 0:
        log("Rust code did not compile.")
        raise Failure("Rust code did not compile.")
    log("Rust code compiled.")
