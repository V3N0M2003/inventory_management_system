class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}
        self.carts = {}
        self.discounts = {}

    def AddItemToInventory(self, productId, quantity):
        if productId in self.inventory:
            self.inventory[productId] += quantity
        else:
            self.inventory[productId] = quantity
        print(f"Added {quantity} of product {productId} to inventory.")

    def RemoveItemFromInventory(self, productId, quantity):
        if productId in self.inventory and self.inventory[productId] >= quantity:
            self.inventory[productId] -= quantity
            if self.inventory[productId] == 0:
                del self.inventory[productId]
            print(f"Removed {quantity} of product {productId} from inventory.")
        else:
            print(f"Cannot remove {quantity} of product {productId} from inventory. Not enough stock or product doesn't exist.")

    def AddItemToCart(self, customerId, productId, quantity):
        if productId in self.inventory and self.inventory[productId] >= quantity:
            if customerId not in self.carts:
                self.carts[customerId] = {}
            if productId in self.carts[customerId]:
                self.carts[customerId][productId] += quantity
            else:
                self.carts[customerId][productId] = quantity
            self.inventory[productId] -= quantity
            print(f"Added {quantity} of product {productId} to customer {customerId}'s cart.")
        else:
            print(f"Cannot add {quantity} of product {productId} to customer {customerId}'s cart. Not enough stock.")

    def ApplyDiscountCoupon(self, cartValue, discountId):
        if discountId in self.discounts:
            discount = self.discounts[discountId]
            discountAmount = (cartValue * discount['DiscountPercentage']) / 100
            if discountAmount > discount['MaximumDiscountCap']:
                discountAmount = discount['MaximumDiscountCap']
            discountedPrice = cartValue - discountAmount
            print(f"Applied discount coupon {discountId}. Original price: {cartValue}, Discounted price: {discountedPrice}")
            return discountedPrice
        else:
            print(f"Discount ID {discountId} not found.")
            return cartValue

    def AddDiscountCoupon(self, discountId, discountPercentage, maxDiscountCap):
        self.discounts[discountId] = {
            'DiscountPercentage': discountPercentage,
            'MaximumDiscountCap': maxDiscountCap
        }
        print(f"Added discount coupon {discountId} with {discountPercentage}% off and max cap {maxDiscountCap}.")


# Driver function to demonstrate the flow of the application
def main():
    ims = InventoryManagementSystem()
    
    # Adding items to inventory
    ims.AddItemToInventory('P001', 50)
    ims.AddItemToInventory('P002', 30)
    
    # Removing items from inventory
    ims.RemoveItemFromInventory('P001', 10)
    
    # Adding items to cart
    ims.AddItemToCart('C001', 'P001', 5)
    ims.AddItemToCart('C002', 'P002', 10)
    
    # Adding discount coupons
    ims.AddDiscountCoupon('D001', 20, 150)
    
    # Applying discount coupons
    cartValue = 2000  # example cart value
    discountedPrice = ims.ApplyDiscountCoupon(cartValue, 'D001')
    
    print(f"Final price after discount: {discountedPrice}")

if __name__ == "__main__":
    main()
