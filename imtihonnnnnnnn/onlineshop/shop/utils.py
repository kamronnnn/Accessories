from .models import Order, OrderProduct, GamingBuilds, LapTop, Monitor, Armchair, Mice, Keyboard, Customer

class CartAuthenticatedUser:
    def __init__(self, request, gaming_id=None, action=None):
        self.request = request

        if gaming_id and action:
            self.add_or_delete(gaming_id, action)

    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(
            user=self.request.user,
        )

        order, created = Order.objects.get_or_create(
            customer=customer,
        )

        order_products = order.orderproduct_set.all()

        return {
            'order': order,
            'order_products': order_products
        }

    def add_or_delete(self, gaming_id, action):
        order = self.get_cart_info()['order']
        gaming_build = GamingBuilds.objects.get(pk=gaming_id)
        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            gaming_build=gaming_build
        )

        if action == 'add':
            order_product.quantity += 1
            gaming_build.quantity -= 1
        else:
            order_product.quantity -= 1
            gaming_build.quantity += 1

        order_product.save()
        gaming_build.save()

