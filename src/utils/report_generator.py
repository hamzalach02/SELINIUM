from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Vulnerability Scan Report', 0, 1, 'C')

    def add_finding(self, finding):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, finding)

def generate_report(findings, output_file):
    pdf = PDFReport()
    pdf.add_page()
    for finding in findings:
        pdf.add_finding(finding)
    pdf.output(output_file)
