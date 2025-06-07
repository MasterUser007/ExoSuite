import sys
import subprocess

def main():
    try:
        subprocess.run(['python', '--version'], check=True)
        print('Python is available')
    except Exception as e:
        print(f'Python validation failed: {e}')
        sys.exit(1)
    print('Validation complete for department: finance')

if __name__ == '__main__':
    main()