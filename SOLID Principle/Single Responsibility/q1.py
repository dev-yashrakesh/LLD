# class Invoice:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def calculate_total(self):
#         return self.amount + (self.amount * 0.18)  # GST
#
#     def save_to_db(self):
#         print("Saving invoice to database")
#
#     def print_invoice(self):
#         print("Printing invoice")


#ANSWER

GST_AMOUNT = 50

class Invoice:
    def __init__(self,data):
        self.data = data
        self.amount=self.data['amount']
        self.invoice_number = self.data['invoice_number']

class InvoicePrint:
    def print(self,invoice : Invoice):
        return f"printing invoice with amount {invoice.amount}"

class InvoiceCalculator:
    def calculator(self,invoice:Invoice):
        return invoice.amount + (GST_AMOUNT + invoice.amount)

class InvoiceRepository:
    def save(self,invoice:Invoice):
        return f"saving invoice to db with invoice number {invoice.invoice_number}"


invoice_data = {
    "amount" : 1000,
    "invoice_number" : 1,
}

invoice = Invoice(invoice_data)
print(invoice)
print = InvoicePrint()
calculator = InvoiceCalculator()
saver = InvoiceRepository()