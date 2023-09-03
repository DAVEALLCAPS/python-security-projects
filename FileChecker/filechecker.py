import hashlib

def calculate_checksum(file_path, algorithm):
    """Calculate the checksum of a file using the given algorithm."""
    
    BUF_SIZE = 65536  # read files in 64kb chunks

    algorithms = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256(),
        'sha512': hashlib.sha512()
    }

    hasher = algorithms.get(algorithm.lower())

    if hasher is None:
        print("Unsupported algorithm. Supported options are: md5, sha1, sha256, sha512.")
        return None

    with open(file_path, 'rb') as f:
        for buf in iter(lambda: f.read(BUF_SIZE), b''):
            hasher.update(buf)
    return hasher.hexdigest()

def main():
    print("File Integrity Checker")
    
    # Getting file path
    file_path = input("Enter the path of the file: ")

    # Displaying supported algorithms and getting user choice
    print("\nSupported algorithms: md5, sha1, sha256, sha512")
    algorithm = input("Enter the desired hashing algorithm: ")

    checksum = calculate_checksum(file_path, algorithm)
    if checksum:
        print(f"{algorithm.upper()} Checksum: {checksum}")

        compare_with = input("Enter known checksum to compare with (or press Enter to skip): ")
        if compare_with:
            if compare_with == checksum:
                print("Checksums match! The file is verified.")
            else:
                print("Checksums do not match! The file may have been altered.")

if __name__ == "__main__":
    main()
