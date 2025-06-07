import subprocess

def run_all_tests():
    print("?? Running all ExoSuite tests...\n")
    subprocess.run(["pytest", "tests"])

if __name__ == "__main__":
    run_all_tests()
