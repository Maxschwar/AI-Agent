from functions.get_file_content import get_file_content

working_dir = "calculator"

def main():
    test_get_file_content = get_file_content(working_dir, "lorem.txt")
    print(test_get_file_content)
    test_main = get_file_content(working_dir, "main.py")
    print(test_main)
    test_pkg_calc = get_file_content(working_dir, "pkg/calculator.py")
    print(test_pkg_calc)
    test_bin = get_file_content(working_dir, "/bin/cat")
    print(test_bin)
    test_error = get_file_content(working_dir, "pkg/does_not_exist.py")
    print(test_error)

main()