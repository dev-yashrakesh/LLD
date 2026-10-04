# class PaymentProcessor:
#     def pay(self, method):
#         if method == "card":
#             return "Card payment"
#
#         elif method == "upi":
#             return "UPI payment"


# answer

class PaymentMethod:
    def pay(self):
        pass

class CardPayment(PaymentMethod):
    def pay(self):
        return "Payment method is card"

class UPIPayment(PaymentMethod):
    def pay(self):
        return "Payment method is upi"

class PaypalPayment(PaymentMethod):
    def pay(self):
        return "Payment method is paypal"

class CryptoPayment(PaymentMethod):
    def pay(self):
        return "Payment method is crypto"

class WalletPayment(PaymentMethod):
    def pay(self):
        return "Payment method is wallet"

class PaymentProcessor:
    def processor(self,payment : PaymentMethod):
        return payment.pay()
