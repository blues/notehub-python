import sys
import subprocess
import shutil
import os


def download_python_template():
    try:
        subprocess.run([
            "openapi-generator-cli",
            "author",
            "template",
            "-g",
            "python",
            "--library",
            "urllib3",
        ])
    except Exception as e:
        print("Exception when generating package: %s\n" % e)


def generate_package():
    try:
        subprocess.run([
            "openapi-generator-cli",
            "generate",
            "-g",
            "python",
            "--library",
            "urllib3",
            "-t",
            "lib_template",
            "-o",
            "src",
            "-i",
            "openapi.yaml",
            "-c",
            "config.json"
        ])
    except Exception as e:
        print("Exception when generating package: %s\n" % e)


def build_distro_package():
    try:
        os.chdir("src/")
        # Check if the 'dist/' folder exists
        if os.path.exists("dist"):
            # If it exists, delete it and its contents
            shutil.rmtree("dist")

        # Upgrade the 'build' module
        subprocess.run([
            "python3",
            "-m",
            "pip",
            "install",
            "--upgrade",
            "build"
        ])

        # Generate a new 'dist/' folder  
        subprocess.run([
            "python3",
            "-m",
            "build"
        ])  
    except Exception as e:
        print("Exception when building distro package: %s\n" % e)    


# todo delete this 
def publish_package():
    try:
        os.chdir("src/")
        subprocess.run([
            "python3",
            "-m",
            "pip",
            "install",
            "--upgrade",
            "twine"
        ])
        subprocess.run([
            "python3",
            "-m",
            "twine",
            "upload",
            "--repository",
            "testpypi",
            "dist/*"
        ])
    except Exception as e:
        print("Exception when publishing package: %s\n" % e)        


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts.py [download_python_template | generate_package | build_distro_package | publish_package]")
        sys.exit(1)
    
    script_to_run = sys.argv[1]
    if script_to_run == "download_python_template":
        download_python_template()
    elif script_to_run == "generate_package":
        generate_package()
    elif script_to_run == "build_distro_package":
        build_distro_package()
    elif script_to_run == "publish_package":
        publish_package()
    else:
        print("Invalid script name. Use one of: download_python_template, generate_package, build_distro_package, publish_package")
        sys.exit(1) 