""" sales total price is a sum of the position's prices
    using many2many_changed
"""
from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_total_price(sender, instance, action, **kwargs):
    """ looping through many to many field (positions) in sales
        to get every ones price and add them up together 
    """
    print(action)

    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        
        for item in instance.get_positions():
            total_price += item.price

    instance.total_price = total_price
    instance.save()
