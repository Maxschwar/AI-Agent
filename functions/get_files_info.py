import os

def get_files_info(working_directory, directory="."):
    try:

        abs_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(abs_path, directory))
        if os.path.commonpath([abs_path, full_path]) == abs_path:
            if os.path.isdir(full_path):
                data = []
                for item in os.listdir(full_path):
                    path = full_path + "/" + item
                    data.append(f"- {item}: file-size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}")
                result = "\n".join(data)
                return f"Result for {directory} directory:\n{result}"
            raise Exception(f'Error: "{directory}" is not a directory')
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    except:
        raise Exception(f'Error: Somthing went wrong')