from fpdf import FPDF


class Shirt:
   def __init__(self, name):
       pdf = FPDF()
       pdf.add_page()
       pdf.set_font('helvetica', "B", size=40)
       pdf.cell(text="CS50 Shirtificate", center=True)
       pdf.image("shirtificate.png", x=0, y=60)
       pdf.set_font('helvetica', size=25)
       with pdf.local_context(text_mode="FILL"):
          pdf.set_text_color(255, 255, 255)
          pdf.cell(None, 240, text=f"{name} took CS50", center=True, new_x="CENTER", new_y="NEXT")
       pdf.output("shirtificate.pdf")










def main():
    name = input("Name: ")
    Shirt(name)









if __name__ == "__main__":
    main()