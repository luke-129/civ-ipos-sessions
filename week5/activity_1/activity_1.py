# Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
from logging import exception


def convert_byte_to_string(byte):
        return byte.decode('unicode-escape')


# Main program logic
def main():
        try:
            # Open the binary file for reading and create output text and bytes files for writing using the context manager
                with open("data.bin", "rb") as data_file:
                        # Iterate through each line in the binary file
                        for line in data_file:
                                # Decode the line to Unicode string and remove leading/trailing whitespaces
                                decoded_line = line.decode("utf-8").strip()


                    # Check if the line starts with "TEXT:"
                                if decoded_line.startswith("TEXT:"):
                                        # Extract text content, convert to uppercase, and write to text file
                                        text_file = open("converted_text.txt", "w")
                                        text_file.write(decoded_line.upper())
                                        text_file.close()


                    # Check if the line starts with "BYTES:"
                    # elif line.startswith("BYTES:"):
                                elif decoded_line.startswith("BYTES:"):
                                        encoded_line = decoded_line.encode("utf-8", 'hex')

                                        print(convert_byte_to_string(encoded_line)[6:])
                                        #Write data to covnerted text file
                                        text_file = open("converted_text.txt", "w")
                                        text_file.write(convert_byte_to_string(encoded_line)[6:])
                                        text_file.close()


                                        hex_line = encoded_line.hex()

                                        bytes_line = encoded_line.fromhex(str(hex_line))

                                        byte_file = open("reversed_bytes.bin", "wb")
                                        byte_file.write(bytes_line)
                                        byte_file.close()



                # Extract the string and encode to hexadecimal

                # Extract byte content, convert to bytes object(using fromhex()),

                # reverse bytes, and write to bytes file


    # Print success message


# Handle file I/O errors

        except UnicodeDecodeError:
                print("Invalid data")


main()