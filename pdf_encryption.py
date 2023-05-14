import PyPDF2

def encrypt_pdf(user_input, output_file, password):
    # Read the input PDF file
    with open(user_input, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF is already encrypted
        if pdf_reader.is_encrypted:
            print("The input PDF file is already encrypted.")
            return

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add the pages from the input PDF to the writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Encrypt the PDF with the provided password
        pdf_writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

    print("The PDF has been encrypted successfully.")

if __name__ == '__main__':
    input_file = 'input.pdf'
    output_file = f'{input_file}ENCRYPTED.pdf'
    password = 'your_password'

    input_file = input("Enter the name of the file (must be in the same directory as the program): ")
    password = input("Enter your pdf's new password: ")

    encrypt_pdf(input_file, output_file, password)
