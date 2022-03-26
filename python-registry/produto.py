import random
class Produto(object):
    def __init__(self,name_company=None,total_product=None,total_product_payment=None,payment_type=None,troco=None,payment_type_value=0):
        self.name_company=name_company
        self.product=[]
        self.total_product=total_product
        self.payment_type=payment_type
        self.payment_type_value=payment_type_value
        self.troco=troco
        self.total_product_payment=total_product_payment
    

    @property
    def payment_type_value(self):
        return self._payment_type_value

    @payment_type_value.setter
    def payment_type_value(self,value):
        if value == 1:
            self.payment_type="Debito"
            self._payment_type_value=0

        elif value == 2:
            self.payment_type="Credito"
            self._payment_type_value=3.54

        elif value == 3:
            self.payment_type="Dinheiro"
            self._payment_type_value=3.12


        elif value == 4:
            self.payment_type="Pix"
            self._payment_type_value=1.85

        else:
            print("Número invalido")
            return False

    @staticmethod
    def generate_id_sales(n):
        range_start=10**(n-1)
        range_end=(10**n)-1
        return random.randint(range_start,range_end)
    
    def sum_sales(self):
        self.total_product=sum(self.product)
        self.taxa_payment()
        count=0
        for  product in self.product:
            count+=1
            print(f'Produto {count}: R$ {product}')
        print(f"Total: {self.total_product_payment}")
    
    def taxa_payment(self):
        print("passou aqui")
        print(self.payment_type)
        if self.payment_type == "Credito":
            print("passou aqui")
            print(self.total_product)
            print(self.payment_type_value)
            print("passou aqui")
            self.total_product_payment=self.total_product+(self.payment_type_value*self.total_product)
            return self.total_product_payment
        elif self.payment_type == "Dinheiro":
           pass
        else:
            self.total_product_payment=self.total_product-(self.payment_type_value*self.total_product)
            return self.total_product_payment
            
          
    def select_product(self):
        print("Digite o numero de produtos no carrinho")
        number_product=int(input())
        try:
            for products in range(number_product):
                products=float(input())
                try:
                    self.product.append(products)
                except:
                    print("tipo invalido")
            print("Digite um número referente a forma de pagamento:")
            print("1 - Débito")
            print("2 - Crédito")
            print("3 - Dinheiro")
            print("4 - Pix")
            self._payment_type=input("Digite um número referente a forma de pagamento:")
            self.sum_sales()
        except ValueError:
            pass
    
    

p=Produto("COMPANY",)
p.select_product()
  