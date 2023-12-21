# Python program to read a file called "random_text.bin",
# split its content by NULL character, and print each line

def process_file(filename):
    try:
        with open(filename, 'rb') as file:  # Open the file in binary mode
            content = file.read()
            lines = content.split(b"\x00")  # Split by NULL character

            # Analytic variables
            total_lines = len(lines)
            current_line_count = 0
            filtered_count = 0
            short_lines = []
            first_chars = ""

            # Create a list of tuples (length, line), then sort by length
            lines_with_length = [(len(line), line.decode('utf-8', errors='replace')) for line in lines]
            # sorted_lines = sorted(lines_with_length, key=lambda x: x[0], reverse=True)

            # Print sorted lines with their length
            for length, line in lines_with_length:
                current_line_count += 1
                if length <= 80:
                    filtered_count += 1
                    short_lines.append((length, line))
                    print(f"{filtered_count}-{current_line_count}-{length}-{line}")

            print(f"Total Lines: {total_lines}")

            # Sorting short_lines by length in ascending order
            sorted_short_lines = sorted(short_lines, key=lambda x: x[0])

            # Print sorted short lines
            print("\nSorted Short Lines:")
            for length, line in sorted_short_lines:
                print(f"{length}-{line}")
                if line:  # Check if line is not empty
                    first_chars += line[0]

            # Print the concatenated first characters
            print("\nConcatenated First Characters:")
            print(first_chars)

    except Exception as e:
        print(f"Error reading file: {e}")


process_file("random_text.bin")
