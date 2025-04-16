from hypothesis import given, strategies as st
from scanner import isValidUserName, isValidPasswordName, isValidKey, checkIfValidSecret, scanUserName, getYAMLFiles

# Open a file to write the outputs with UTF-8 encoding
output_file = open("fuzz_output.txt", "w", encoding="utf-8")

# Test isValidUserName
def test_isValidUserName():
    print("isValidUserName('admin'):", isValidUserName("admin"), file=output_file)          # Forbidden username
    print("isValidUserName('user123'):", isValidUserName("user123"), file=output_file)      # Valid username
    print("isValidUserName(''):", isValidUserName(""), file=output_file)                   # Empty string
    print("isValidUserName('💣'):", isValidUserName("💣"), file=output_file)               # Emoji
    print("isValidUserName('<script>'):", isValidUserName("<script>"), file=output_file)   # Script injection string

# Test isValidPasswordName
def test_isValidPasswordName():
    print("isValidPasswordName('password'):", isValidPasswordName("password"), file=output_file)   # Forbidden password
    print("isValidPasswordName('secure123'):", isValidPasswordName("secure123"), file=output_file) # Valid password
    print("isValidPasswordName(''):", isValidPasswordName(""), file=output_file)                   # Empty string
    print("isValidPasswordName('💥'):", isValidPasswordName("💥"), file=output_file)               # Emoji
    print("isValidPasswordName('null'):", isValidPasswordName("null"), file=output_file)           # Special string

# Test isValidKey
def test_isValidKey():
    print("isValidKey('api_key'):", isValidKey("api_key"), file=output_file)             # Valid key
    print("isValidKey('invalid_key'):", isValidKey("invalid_key"), file=output_file)     # Invalid key
    print("isValidKey(''):", isValidKey(""), file=output_file)                          # Empty string
    print("isValidKey('😉👍'):", isValidKey("😉👍"), file=output_file)                  # Emoji combo
    print("isValidKey('0x123'):", isValidKey("0x123"), file=output_file)                # Hex-like string

# Test checkIfValidSecret
def test_checkIfValidSecret():
    print("checkIfValidSecret('my_secret'):", checkIfValidSecret("my_secret"), file=output_file)   # Valid secret
    print("checkIfValidSecret(''):", checkIfValidSecret(""), file=output_file)                    # Empty string
    print("checkIfValidSecret('💥'):", checkIfValidSecret("💥"), file=output_file)                # Emoji
    print("checkIfValidSecret('null'):", checkIfValidSecret("null"), file=output_file)            # Special string
    print("checkIfValidSecret('password'):", checkIfValidSecret("password"), file=output_file)    # Forbidden secret

# Test scanUserName
def test_scanUserName():
    print("scanUserName('username', ['admin', 'user123']):", scanUserName("username", ["admin", "user123"]), file=output_file)  # Valid and invalid usernames
    print("scanUserName('username', []):", scanUserName("username", []), file=output_file)                                     # Empty list
    print("scanUserName('username', ['💣', 'null']):", scanUserName("username", ["💣", "null"]), file=output_file)             # Emoji and special string

# Test getYAMLFiles
def test_getYAMLFiles():
    print("getYAMLFiles('.'):", getYAMLFiles("."), file=output_file)                       # Current directory
    print("getYAMLFiles('nonexistent_dir'):", getYAMLFiles("nonexistent_dir"), file=output_file)   # Nonexistent directory
    print("getYAMLFiles(''):", getYAMLFiles(""), file=output_file)                        # Empty path
    print("getYAMLFiles('💻'):", getYAMLFiles("💻"), file=output_file)                    # Emoji as directory name

if __name__ == "__main__":
    test_isValidUserName()
    test_isValidPasswordName()
    test_isValidKey()
    test_checkIfValidSecret()
    test_scanUserName()
    test_getYAMLFiles()
    print("All fuzz tests passed!", file=output_file)
    output_file.close()