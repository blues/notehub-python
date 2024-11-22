import sys
import subprocess
import shutil
import os
import yaml


def download_python_template():
    """
    Download the Python client library template from the OpenAPI Generator.
    """
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
    """
    Generate the Python client library package using the OpenAPI Generator.
    """
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
            "openapi_filtered.yaml",
            "-c",
            "config.json"
        ])
    except Exception as e:
        print("Exception when generating package: %s\n" % e)


def build_distro_package():
    """
    Build the distribution package for the Notehub Py client library.
    """
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


def remove_deprecated_parameters(input_file: str, output_file: str):
    """
    Load an OpenAPI YAML file, remove deprecated parameters, and save to a new file.
    """
    with open(input_file, 'r') as f:
        openapi_spec = yaml.safe_load(f)

    # Traverse paths and operations to remove deprecated parameters
    for path, methods in openapi_spec.get('paths', {}).items():
        for method, operation in methods.items():
            if isinstance(operation, dict):
                # Remove deprecated parameters
                if 'parameters' in operation:
                    operation['parameters'] = [
                        param for param in operation['parameters']
                        if not param.get('deprecated', False)
                    ]
                
                # Remove deprecated requestBody properties if applicable
                if 'requestBody' in operation:
                    content = operation['requestBody'].get('content', {})
                    for content_type, schema in content.items():
                        properties = schema.get('schema', {}).get(
                            'properties', {}
                        )
                        schema['schema']['properties'] = {
                            k: v for k, v in properties.items() 
                            if not v.get('deprecated', False)
                        }

    # Save the modified spec to a new file
    with open(output_file, 'w') as f:
        yaml.dump(openapi_spec, f, sort_keys=False)

    print(f"Filtered OpenAPI spec saved to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python3 scripts.py [download_python_template | " 
            "generate_package | build_distro_package | "
            "remove_deprecated_parameters]"
        )
        sys.exit(1)
    
    script_to_run = sys.argv[1]
    if script_to_run == "download_python_template":
        download_python_template()
    elif script_to_run == "generate_package":
        generate_package()
    elif script_to_run == "build_distro_package":
        build_distro_package()
    elif script_to_run == "remove_deprecated_parameters":
        remove_deprecated_parameters("openapi.yaml", "openapi_filtered.yaml")    
    else:
        print(
            "Invalid script name. Use one of: download_python_template, "
            "generate_package, build_distro_package, "
            "remove_deprecated_parameters"
        )
        sys.exit(1) 