from fpdf import FPDF

class CertificatePDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format)

    def set_helvetica_font(self, style, size):
        self.set_font("Helvetica", style, size)

    def _print(self, user_name):
        text = f"{user_name} took the CS50"
        self.cell(0, 10, text, 0, align='C')
        self.ln(10)

    def add_certificate_content(self, title, image_path, user_name):
        self.add_page()

        # Use Helvetica as a substitute for Arial
        self.set_helvetica_font("B", 16)

        # Add title at the top, centered horizontally
        title_width = self.get_string_width(title)
        self.cell(0, 10, title, 0, align='C')
        self.ln(10)

        # Add the image centered horizontally
        image_width = 90  # Width of the image
        x_position = (self.w - image_width) / 2
        self.image(image_path, x=x_position, y=self.get_y(), w=image_width)

        # Move to the position for the user's name
        self.ln(30)

        # Set font color to white
        self.set_text_color(255, 255, 255)

        # Use Helvetica as a substitute for Arial
        self.set_helvetica_font("", 14)

        # Use new_x and new_y instead of ln
        self._print(user_name)

        # Reset font color to black
        self.set_text_color(0, 0, 0)

    def save_certificate(self, output_filename):
        self.output(output_filename)


def generate_certificate(user_name):
    certificate_pdf = CertificatePDF()

    # Generate the shirtificate with the user's name
    certificate_pdf.add_certificate_content("CS50 Shirtificate", "shirtificate.png", user_name)
    certificate_pdf.save_certificate("shirtificate.pdf")

if __name__ == "__main__":
    # Get user's name
    user_name = input("Enter your name: ")

    generate_certificate(user_name)
