# inventory_management_system

# Overview
This is a simple inventory management system for an e-commerce store. The system allows administrators to add and remove products from inventory, and customers to add items to their carts. Additionally, the system supports applying discount coupons to cart values.

# Data Structures
Inventory: A dictionary (inventory) to keep track of product IDs and their quantities.
Carts: A dictionary (carts) where each key is a customer ID, and the value is another dictionary representing the customer's cart (product IDs and quantities).
Discount Coupons: A dictionary (discounts) to store discount details with discount IDs.

# APIs
1. AddItemToInventory(productId, quantity)
    Adds a specified quantity of a product to the inventory.

2. RemoveItemFromInventory(productId, quantity)
    Removes a specified quantity of a product from the inventory.

3. AddItemToCart(customerId, productId, quantity)
    Adds items to a customer's cart after checking inventory availability.

3. ApplyDiscountCoupon(cartValue, discountId)
    Applies a discount coupon to the total cart value.
