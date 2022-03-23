import random
class Produto(object):
    def __init__(self,name_company=None,total_product=None,payment_type=None,troco=None):
        self.name_company=name_company
        self.product=[]
        self.total_product=total_product
        self.payment_type=payment_type
        self.troco=troco
    

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self,value):
        print(value)
        if value == 1:
            self._payment_type=0
            pass
        elif value == 2:
            self._payment_type=3.54
            pass
        elif value == 3:
            self._payment_type=3.12
            pass
        elif value == 4:
            self._payment_type=1.85
            pass
        else:
            print("Número invalido")
            return False

    @staticmethod
    def generate_id_sales(n):
        range_start=10**(n-1)
        range_end=(10**n)-1
        return random.randint(range_start,range_end)
    
    def sum_sales(self):
        print(self.product)
        self.total_product=sum(self.product)
        print(self.name_company)
        count=0
        for  product in self.product:
            count+=1
            print(f'Produto {count}: R$ {product}')
        print(f"Total: {self.total_product}")
          
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
  