from fpdf import FPDF

# Class named Shirtificate
class Shirtificate(FPDF):

     # Initiate function
	def __init__(self, nameInfo):

		super().__init__()

          # Info for shirts
		self.add_page()

		self.set_font("helvetica", "B", 50)

		self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

		self.image("shirtificate.png", w=self.epw)

		self.set_font_size(30)

		self.set_text_color(255, 255, 255)

		self.text(x=47.5, y=140, txt=f"{nameInfo} took CS50")




# User input info for shirt
Shirts = Shirtificate(input("Name: "))

# Output for a shirt
Shirts.output("shirtificate.pdf")